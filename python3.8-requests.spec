%undefine _missing_build_ids_terminate_build
%define debug_package %{nil}

Name:           python3.8-requests
Version:        2.23.0
Release:        2%{?dist}
Summary:        HTTP library, written in Python, for human beings

License:        ASL 2.0
URL:            https://pypi.io/project/requests
Source0:        https://github.com/requests/requests/archive/v%{version}/requests-v%{version}.tar.gz
BuildRequires:  python3.8-devel

BuildArch:      noarch

%description
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python’s built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.


%prep
mkdir -p python3.8-requests
%setup -T -D -n python3.8-requests


%build

	
%install
mkdir -p %{buildroot}/usr/lib/python3.8/site-packages/
mkdir -p %{buildroot}/usr/bin/
/usr/bin/python3.8 -m pip install --user chardet urllib3 idna Pygments 'requests==2.23.0' 
pushd $HOME
cp -rf .local/lib/python3.8/site-packages/* %{buildroot}/usr/lib/python3.8/site-packages/
cp -f .local/bin/chardetect %{buildroot}/usr/bin/chardetect3.8
cp -f .local/bin/pygmentize %{buildroot}/usr/bin/pygmentize3.8

find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!/usr/bin/python3.8=' {} +

%files
/usr/bin/chardetect3.8
/usr/bin/pygmentize3.8
/usr/lib/python3.8/site-packages/Pygments-*.dist-info/
/usr/lib/python3.8/site-packages/pygments/
/usr/lib/python3.8/site-packages/certifi-*.dist-info/
/usr/lib/python3.8/site-packages/certifi/
/usr/lib/python3.8/site-packages/chardet-3.0.4.dist-info/
/usr/lib/python3.8/site-packages/chardet/
/usr/lib/python3.8/site-packages/idna-*.dist-info/
/usr/lib/python3.8/site-packages/idna/
/usr/lib/python3.8/site-packages/requests-2.23.0.dist-info/
/usr/lib/python3.8/site-packages/requests/
/usr/lib/python3.8/site-packages/urllib3-*.dist-info/
/usr/lib/python3.8/site-packages/urllib3/


%changelog
