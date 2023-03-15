#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dcurver
Version  : 0.9.2
Release  : 31
URL      : https://cran.r-project.org/src/contrib/dcurver_0.9.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dcurver_0.9.2.tar.gz
Summary  : Utility Functions for Davidian Curves
Group    : Development/Tools
License  : GPL-3.0
Requires: R-dcurver-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : buildreq-R

%description
easy to estimate parameters. Since a special case of a Davidian curve is the standard normal density,
  Davidian curves can be used for relaxing normality assumption in statistical applications (Zhang & Davidian, 2001)

%package lib
Summary: lib components for the R-dcurver package.
Group: Libraries

%description lib
lib components for the R-dcurver package.


%prep
%setup -q -c -n dcurver
cd %{_builddir}/dcurver

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640997271

%install
export SOURCE_DATE_EPOCH=1640997271
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dcurver
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dcurver
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dcurver
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dcurver || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dcurver/DESCRIPTION
/usr/lib64/R/library/dcurver/INDEX
/usr/lib64/R/library/dcurver/Meta/Rd.rds
/usr/lib64/R/library/dcurver/Meta/features.rds
/usr/lib64/R/library/dcurver/Meta/hsearch.rds
/usr/lib64/R/library/dcurver/Meta/links.rds
/usr/lib64/R/library/dcurver/Meta/nsInfo.rds
/usr/lib64/R/library/dcurver/Meta/package.rds
/usr/lib64/R/library/dcurver/NAMESPACE
/usr/lib64/R/library/dcurver/NEWS.md
/usr/lib64/R/library/dcurver/R/dcurver
/usr/lib64/R/library/dcurver/R/dcurver.rdb
/usr/lib64/R/library/dcurver/R/dcurver.rdx
/usr/lib64/R/library/dcurver/help/AnIndex
/usr/lib64/R/library/dcurver/help/aliases.rds
/usr/lib64/R/library/dcurver/help/dcurver.rdb
/usr/lib64/R/library/dcurver/help/dcurver.rdx
/usr/lib64/R/library/dcurver/help/paths.rds
/usr/lib64/R/library/dcurver/html/00Index.html
/usr/lib64/R/library/dcurver/html/R.css
/usr/lib64/R/library/dcurver/tests/testthat.R
/usr/lib64/R/library/dcurver/tests/testthat/test_inputs.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/dcurver/libs/dcurver.so
/usr/lib64/R/library/dcurver/libs/dcurver.so.avx2
/usr/lib64/R/library/dcurver/libs/dcurver.so.avx512
