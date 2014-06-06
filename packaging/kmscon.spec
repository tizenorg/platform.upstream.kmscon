Name:           kmscon
Version:        8.0
Release:        0
Summary:        KMS/DRM based System Console 
License:        MIT
Group:          Graphics & UI Framework/Wayland Window System
Url:            http://www.freedesktop.org/wiki/Software/kmscon

#Git-Clone:	git://people.freedesktop.org/~dvdhrm/kmscon
#Git-Web:	http://cgit.freedesktop.org/~dvdhrm/kmscon
Source0:         %name-%version.tar.xz
Source1001:     kmscon.manifest
BuildRequires:	autoconf >= 2.64, automake >= 1.11
BuildRequires:  expat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool >= 2.2
BuildRequires:  libvpx-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:	pkgconfig(libtsm)
BuildRequires:  pkgconfig(libudev) >= 136
BuildRequires:  pkgconfig(libdrm) >= 2.4.30
BuildRequires:  pkgconfig(egl) >= 7.10
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gbm)	
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.0
BuildRequires:  kernel-headers
BuildRequires:  pkgconfig(pangocairo)

%description
kmscon is a system console for linux. It doesn't depend on any
graphic-server on your system(like X.org), but instead provides a raw
console layer that can be used independently. It can replace the linux
kernel console entirely but was designed to work well side-by-side.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen 
make %{?_smp_mflags} 

%install
%make_install

%define _unitdir_system /usr/lib/systemd/system
install -d %{buildroot}%{_unitdir_system}
install -m 644 docs/kmscon.service %{buildroot}%{_unitdir_system}
install -m 644 docs/kmsconvt@.service %{buildroot}%{_unitdir_system}

%define _unit_config /etc/systemd/system
install -d %{buildroot}%{_unit_config}
ln -s %{_unitdir_system}/kmsconvt@.service %{buildroot}%{_unit_config}/autovt@.service

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%_bindir/%{name}
%_libdir/%{name}/
%{_unitdir_system}/
%{_unit_config}/autovt@.service

%changelog
