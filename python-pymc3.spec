%global modname pymc3

%global commit 7427adb98c3fc6a7617415e9309c2bf0dc80d8bb
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        3.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Easy to use wrappers generator for C libraries based on ctypes

License:        ASL 2.0
URL:            https://github.com/pymc-devs/pymc3
Source0:        https://github.com/pymc-devs/pymc3/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
BuildRequires:  python2-nose python-mock
%if 0%{?fedora} > 23
BuildRequires:  python2-numpy python2-scipy
BuildRequires:  python2-pandas
Requires:       python2-numpy python2-scipy
Requires:       python2-pandas
%else
BuildRequires:  numpy scipy
BuildRequires:  python-pandas
Requires:       numpy scipy
Requires:       python-pandas
%endif
BuildRequires:  python-matplotlib
BuildRequires:  python2-theano
BuildRequires:  python-enum34
Requires:       python-matplotlib
Requires:       python2-theano
Requires:       python-enum34

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-numpy python3-scipy
BuildRequires:  python3-pandas
BuildRequires:  python3-matplotlib
BuildRequires:  python3-theano
Requires:       python3-numpy python3-scipy
Requires:       python3-pandas
Requires:       python3-matplotlib
Requires:       python3-theano

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{modname}
%license LICENSE
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%{python3_sitelib}/%{modname}*

%changelog
* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.0-0.1.git7427adb
- Initial package
