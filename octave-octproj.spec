%global octpkg octproj

Summary:	Use PROJ library for cartographic projections transformations in Octave
Name:		octave-octproj
Version:	3.0.2
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/octproj/
Url:		https://bitbucket.org/jgpallero/octproj/src/master/
Source0:	https://bitbucket.org/jgpallero/octproj/downloads/octproj-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?55344
Patch0:		do-not-strip-debugging-symbols.patch

BuildRequires:  octave-devel >= 3.0.0
BuildRequires:	pkgconfig(proj)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
This package allows to call functions of PROJ library for
cartographic projections and CRS transformations.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

