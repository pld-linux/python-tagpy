Summary:	Python bindings for TagLib
Summary(pl.UTF-8):	Wiązania Pythona dla biblioteki TagLib
Name:		python-tagpy
Version:	0.91
Release:	0.1
License:	BSD-Style
Group:		Libraries/Python
Source0:	http://news.tiker.net/news.tiker.net/download/software/tagpy/tagpy-%{version}.tar.gz
# Source0-md5:	c9de0b7b3819579b5f460b20c42e03c9
URL:		http://news.tiker.net/software/tagpy
BuildRequires:	boost-python-devel
BuildRequires:	boost-bind-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	taglib-devel
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TagPy is a set of Python bindings for Scott Wheeler’s TagLib. It builds upon
Boost.Python, a wrapper generation library which is part of the Boost set of
C++ libraries.

Just like TagLib, TagPy can:

    * read and write ID3 tags of version 1 and 2, with many supported frame
      types for version 2 (in MPEG Layer 2 and MPEG Layer 3, FLAC and MPC),
    * access Xiph Comments in Ogg Vorbis Files and Ogg Flac Files,
    * access APE tags in Musepack and MP3 files.

All these features have their own specific interfaces, but TagLib’s generic tag
reading and writing mechanism is also supported. It comes with a bunch of
examples.

%prep
%setup -n tagpy-%{version} -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
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
%{py_sitedir}/tagpy*egg-info
