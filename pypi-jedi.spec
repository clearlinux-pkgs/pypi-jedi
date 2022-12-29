#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jedi
Version  : 0.18.2
Release  : 37
URL      : https://files.pythonhosted.org/packages/15/02/afd43c5066de05f6b3188f3aa74136a3289e6c30e7a45f351546cab0928c/jedi-0.18.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/15/02/afd43c5066de05f6b3188f3aa74136a3289e6c30e7a45f351546cab0928c/jedi-0.18.2.tar.gz
Summary  : An autocompletion tool for Python that can be used for text editors.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-jedi-license = %{version}-%{release}
Requires: pypi-jedi-python = %{version}-%{release}
Requires: pypi-jedi-python3 = %{version}-%{release}
Requires: pypi(parso)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(parso)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Jedi - an awesome autocompletion, static analysis and refactoring library for Python
        ####################################################################################

%package license
Summary: license components for the pypi-jedi package.
Group: Default

%description license
license components for the pypi-jedi package.


%package python
Summary: python components for the pypi-jedi package.
Group: Default
Requires: pypi-jedi-python3 = %{version}-%{release}

%description python
python components for the pypi-jedi package.


%package python3
Summary: python3 components for the pypi-jedi package.
Group: Default
Requires: python3-core
Provides: pypi(jedi)
Requires: pypi(parso)

%description python3
python3 components for the pypi-jedi package.


%prep
%setup -q -n jedi-0.18.2
cd %{_builddir}/jedi-0.18.2
pushd ..
cp -a jedi-0.18.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672283856
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jedi
cp %{_builddir}/jedi-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jedi/3b2dc8675a3f0d40a28f710a5582bcc56b51a171 || :
cp %{_builddir}/jedi-%{version}/jedi/third_party/django-stubs/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jedi/510c53b9ce77cab0fc399b1ea7d30856e4b11777 || :
cp %{_builddir}/jedi-%{version}/jedi/third_party/typeshed/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jedi/5a77f6d363db008935cc2907446e3965958f3f10 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jedi/3b2dc8675a3f0d40a28f710a5582bcc56b51a171
/usr/share/package-licenses/pypi-jedi/510c53b9ce77cab0fc399b1ea7d30856e4b11777
/usr/share/package-licenses/pypi-jedi/5a77f6d363db008935cc2907446e3965958f3f10

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
