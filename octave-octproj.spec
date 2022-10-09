%define octpkg octproj

Summary:	Use PROJ.4 library for cartographic projections transformations in Octave
Name:		octave-%{octpkg}
Version:	2.0.1
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?61488
Patch0:		honor-cflags-cxxflags.patch
# https://savannah.gnu.org/bugs/index.php?61488
Patch1:		honor-ldflags.patch
# https://savannah.gnu.org/bugs/index.php?61489
Patch2:		format-security-error.patch
# https://savannah.gnu.org/bugs/index.php?55344
Patch3:		do-not-strip-debugging-symbols.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.0.0
buildRequires:	pkgconfig(proj)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
This package allows to call functions of PROJ.4 library for  cartographic
projections transformations.

This package is part of external Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

