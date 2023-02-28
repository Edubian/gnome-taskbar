Name:           gnome-shell-extension-zorin-taskbar
Version:        4.5.0
Release:        4%{?dist}
Summary:        Zorin Taskbar extension. A taskbar extension for the Zorin Desktop environment.
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       gnome-shell

%description
A demo RPM build

%prep
%setup -q

%install
rm -rf "$HOME/.local/share/gnome-shell/extensions/zorin-taskbar@zorinos.com"
mkdir -p "$HOME/.local/share/gnome-shell/extensions/zorin-taskbar@zorinos.com"
cp _build/* "$HOME/.local/share/gnome-shell/extensions/zorin-taskbar@zorinos.com/"

%clean
rm -rf $RPM_BUILD_ROOT

%files
$HOME/.local/share/gnome-shell/extensions/zorin-taskbar@zorinos.com/*

%changelog
* Sun Nov  18 2020 Valentin Bajrami <valentin.bajrami@slimmer.ai> - 0.0.1
- First version being packaged