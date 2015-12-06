%global modname pymc3

%global commit 7427adb98c3fc6a7617415e9309c2bf0dc80d8bb
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        3.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Bayesian statistical modeling and model fitting

License:        ASL 2.0
URL:            https://github.com/pymc-devs/pymc3
Source0:        https://github.com/pymc-devs/pymc3/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
PyMC3 is a python module for Bayesian statistical modeling and model fitting
which focuses on advanced Markov chain Monte Carlo fitting algorithms. Its
flexibility and extensibility make it applicable to a large suite of problems.

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
BuildRequires:  python-theano
BuildRequires:  python-enum34
BuildRequires:  python2-patsy
Requires:       python-matplotlib
Requires:       python-theano
Requires:       python-enum34
Requires:       python2-patsy

%description -n python2-%{modname}
PyMC3 is a python module for Bayesian statistical modeling and model fitting
which focuses on advanced Markov chain Monte Carlo fitting algorithms. Its
flexibility and extensibility make it applicable to a large suite of problems.

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
BuildRequires:  python3-patsy
Requires:       python3-numpy python3-scipy
Requires:       python3-pandas
Requires:       python3-matplotlib
Requires:       python3-theano
Requires:       python3-patsy

%description -n python3-%{modname}
PyMC3 is a python module for Bayesian statistical modeling and model fitting
which focuses on advanced Markov chain Monte Carlo fitting algorithms. Its
flexibility and extensibility make it applicable to a large suite of problems.

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
