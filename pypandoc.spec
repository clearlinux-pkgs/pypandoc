#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypandoc
Version  : 1.4
Release  : 16
URL      : https://pypi.debian.net/pypandoc/pypandoc-1.4.tar.gz
Source0  : https://pypi.debian.net/pypandoc/pypandoc-1.4.tar.gz
Summary  : Thin wrapper for pandoc.
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypandoc-license = %{version}-%{release}
Requires: pypandoc-python = %{version}-%{release}
Requires: pypandoc-python3 = %{version}-%{release}
Requires: pip
Requires: setuptools
Requires: wheel
BuildRequires : buildreq-distutils3
BuildRequires : pandoc
BuildRequires : pip
BuildRequires : setuptools
BuildRequires : wheel

%description
========
        
        |Build Status| |Appveyor Build Status| |GitHub Releases| |PyPI version|
        |conda version| |Development Status| |Python version| |License|

%package license
Summary: license components for the pypandoc package.
Group: Default

%description license
license components for the pypandoc package.


%package python
Summary: python components for the pypandoc package.
Group: Default
Requires: pypandoc-python3 = %{version}-%{release}

%description python
python components for the pypandoc package.


%package python3
Summary: python3 components for the pypandoc package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pypandoc package.


%prep
%setup -q -n pypandoc-1.4
cd %{_builddir}/pypandoc-1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574288435
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypandoc
cp %{_builddir}/pypandoc-1.4/LICENSE %{buildroot}/usr/share/package-licenses/pypandoc/e8a9d3357b730b175b1c2e283b8e0a8daf59c643
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypandoc/e8a9d3357b730b175b1c2e283b8e0a8daf59c643

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
