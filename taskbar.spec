Name:           gnome-shell-extension-zorin-taskbar
Version:        4.5.0
Release:        4%{?dist}
Summary:        A simple hello world script
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

%description
A demo RPM build

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name}.sh $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/_build/*
%{_bindir}/COPYING
%{_bindir}/README.md

%changelog
* Sun Nov  18 2020 Valentin Bajrami <valentin.bajrami@slimmer.ai> - 0.0.1
- First version being packaged