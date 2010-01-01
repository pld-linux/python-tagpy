# TODO: optflags
Summary:	Python bindings for TagLib
Summary(pl.UTF-8):	Wiązania Pythona dla biblioteki TagLib
Name:		python-tagpy
Version:	0.94.5
Release:	3
License:	BSD-Style
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/t/tagpy/tagpy-%{version}.tar.gz
# Source0-md5:	84d7862786ad7bab91d0d45ded15a875
URL:		http://news.tiker.net/software/tagpy
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	boost-python-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools >= 1:0.6-2.c8
BuildRequires:	rpm-pythonprov
BuildRequires:	taglib-devel
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TagPy is a set of Python bindings for Scott Wheeler's TagLib. It
builds upon Boost.Python, a wrapper generation library which is part
of the Boost set of C++ libraries.

Just like TagLib, TagPy can:
 - read and write ID3 tags of version 1 and 2, with many supported
   frame types for version 2 (in MPEG Layer 2 and MPEG Layer 3, FLAC
   and MPC),
 - access Xiph comments in Ogg Vorbis files and Ogg Flac files,
 - access APE tags in Musepack and MP3 files.

%description -l pl.UTF-8
TagPy to zestaw wiązań Pythona do biblioteki TagLib Scotta Wheelera.
Powstał w oparciu o Boost.Python - bibliotekę generowania wrapperów
będącą częścią bibliotek C++ Boost.

Podobnie jak TagLib TagPy pozwala na:
 - odczyt i zapis znaczników ID3 w wersji 1 i 2 z wieloma
   obsługiwanymi typami ramek dla wersji 2 (MPEG Layer 2 i 3, FLAC
   oraz MPC),
 - dostęp do komentarzy Xiph w plikach Ogg Vorbis i Ogg Flac,
 - dostęp do znaczników APE w plikach Musepack i MP3.

%prep
%setup -n tagpy-%{version} -q

%build
# this isn't autoconf generated
./configure \
	--taglib-inc-dir=`pkg-config --variable=includedir taglib`/taglib \
	--boost-python-libname=boost_python
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_tagpy.so
%dir %{py_sitedir}/tagpy
%{py_sitedir}/tagpy/*.py[co]
%dir %{py_sitedir}/tagpy/ogg
%{py_sitedir}/tagpy/ogg/*.py[co]
%{py_sitedir}/tagpy*.egg-info
