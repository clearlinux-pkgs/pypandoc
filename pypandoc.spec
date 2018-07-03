#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypandoc
Version  : 1.4
Release  : 9
URL      : https://pypi.debian.net/pypandoc/pypandoc-1.4.tar.gz
Source0  : https://pypi.debian.net/pypandoc/pypandoc-1.4.tar.gz
Summary  : Thin wrapper for pandoc.
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypandoc-python3
Requires: pypandoc-license
Requires: pypandoc-python
Requires: pip
Requires: setuptools
Requires: wheel
BuildRequires : pandoc
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
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
Requires: pypandoc-python3

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530329463
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pypandoc
cp LICENSE %{buildroot}/usr/share/doc/pypandoc/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/pypandoc/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
