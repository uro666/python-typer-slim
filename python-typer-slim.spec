%define module typer-slim
%define oname typer_slim
#disable test on abf
%bcond_with test

# NOTE Update the python-typer package after this package to keep them in sync.
# NOTE Upstream python-typer & python-typer-slim releases are version synced.

Name:		python-typer-slim
Version:	0.15.2
Release:	1
Summary:	Typer, build great CLIs. Easy to code. Based on Python type hints
URL:		https://pypi.org/project/typer-slim/
License:	None
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/t/typer-slim/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pre-commit)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(click) >= 8.0.0
BuildRequires:	python%{pyver}dist(typing-extensions) >= 3.7.4.3
BuildRequires:	python%{pyver}dist(rich) >= 10.11.0
BuildRequires:	python%{pyver}dist(shellingham) >= 1.3.0
%if %{with test}
BuildRequires:	python%{pyver}dist(click) >= 8.0.0
BuildRequires:	python%{pyver}dist(markdown-it-py)
BuildRequires:	python%{pyver}dist(mdurl)
BuildRequires:	python%{pyver}dist(pygments)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-xdist)
BuildRequires:	python%{pyver}dist(rich) >= 10.11.0
BuildRequires:	python%{pyver}dist(shellingham) >= 1.3.0
BuildRequires:	python%{pyver}dist(typing-extensions) >= 3.7.4.3
%endif
Requires:	python%{pyver}dist(click) >= 8.0.0
Requires:	python%{pyver}dist(typing-extensions) >= 3.7.4.3
Suggests:	python%{pyver}dist(rich) >= 10.11.0
Suggests:	python%{pyver}dist(shellingham) >= 1.3.0

%description
Typer is a library for building CLI applications that users will love using
and developers will love creating. Based on Python type hints.

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py_build

%install
%py3_install
# The typer command is only supposed to be provided by the python-typer package.
rm -rf %{buildroot}/%{_bindir}/typer

%if %{with test}
%check
pip install -e .[test]
%{__python} -m pytest --import-mode append -v -rs -k 'not test_show_completion and not test_install_completion' #"${ignore-}"
%endif

%files
%{py_sitedir}/typer
%{py_sitedir}/%{oname}-%{version}.dist-info
%license LICENSE
%doc README.md
