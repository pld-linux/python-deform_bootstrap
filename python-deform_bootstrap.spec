# TODO
# - jquery, jquery-ui

# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define 	module	deform_bootstrap
Summary:	Twitter Bootstrap compatible widgets, templates and styles for the deform form library
Name:		python-%{module}
Version:	0.2.5
Release:	2
License:	BSD-derived (http://www.repoze.org/LICENSE.txt)
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/d/deform_bootstrap/%{module}-%{version}.tar.gz
# Source0-md5:	82b77818ae4d865127888c86b6598a07
URL:		http://pypi.python.org/pypi/deform_bootstrap
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-deform
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
deform_bootstrap provides Twitter Bootstrap compatible widgets,
templates and styles for the deform form library.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/demo
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/static/*.less

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst  CHANGES.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
%{py_sitescriptdir}/%{module}/templates
%dir %{py_sitescriptdir}/%{module}/static
%{py_sitescriptdir}/%{module}/static/bootstrap-datepicker.css
%{py_sitescriptdir}/%{module}/static/bootstrap-datepicker.js
%{py_sitescriptdir}/%{module}/static/bootstrap-typeahead.js
%{py_sitescriptdir}/%{module}/static/bootstrap.min.js
%{py_sitescriptdir}/%{module}/static/chosen_bootstrap.css
%{py_sitescriptdir}/%{module}/static/deform_bootstrap.css
%{py_sitescriptdir}/%{module}/static/deform_bootstrap.js
%{py_sitescriptdir}/%{module}/static/jquery-1.7.1.min.js
%{py_sitescriptdir}/%{module}/static/jquery-ui-1.8.18.custom.min.js
%{py_sitescriptdir}/%{module}/static/jquery-ui-timepicker-addon-0.9.9.js
%{py_sitescriptdir}/%{module}/static/jquery.form-2.96.js
%{py_sitescriptdir}/%{module}/static/jquery.maskedinput-1.3.js
%dir %{py_sitescriptdir}/%{module}/static/jquery_chosen
%{py_sitescriptdir}/%{module}/static/jquery_chosen/chosen-sprite.png
%{py_sitescriptdir}/%{module}/static/jquery_chosen/chosen.css
%{py_sitescriptdir}/%{module}/static/jquery_chosen/chosen.jquery.js
%{py_sitescriptdir}/%{module}/static/jquery_chosen/chosen.jquery.min.js
