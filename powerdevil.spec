%define major 5
%define stable %([ "%(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: powerdevil
Version: 5.27.7
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
Summary: KDE 5 Power Saving Tools
URL: http://kde.org/
License: GPL
Group: System/Libraries
Patch1: powerdevil-5.5.2-power-settings.patch
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5DNSSD)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5IdleTime)
BuildRequires: cmake(KScreenLocker) < 5.27.50
BuildRequires: cmake(KF5Screen) >= 5.6.0-2
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(LibKWorkspace) < 5.27.50
BuildRequires: cmake(KF5BluezQt)
BuildRequires: cmake(KF5NetworkManagerQt)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libcap)
Requires(meta): power-profiles-daemon
Recommends: kinfocenter
Recommends: networkmanager-qt
Recommends: bluez-qt

%rename plasma-krunner-powerdevil

%description
KDE 5 Power Saving Tools.

%libpackage powerdevilconfigcommonprivate 5
%libpackage powerdevilcore 2
%libpackage powerdevilui 5

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# We don't have headers
rm -f %{buildroot}%{_libdir}/libpowerdevilconfigcommonprivate.so
rm -f %{buildroot}%{_libdir}/libpowerdevilcore.so
rm -f %{buildroot}%{_libdir}/libpowerdevilui.so

%find_lang %{name} --all-name --with-html --with-man

%files -f %{name}.lang
%{_datadir}/dbus-1/system.d/*.conf
%{_sysconfdir}/xdg/autostart/powerdevil.desktop
%caps(cap_wake_alarm+ep) %{_libdir}/libexec/org_kde_powerdevil
%{_libdir}/libexec/kauth/backlighthelper
%{_libdir}/libexec/kauth/discretegpuhelper
%{_libdir}/qt5/plugins/powerdevil*.so
%{_libdir}/qt5/plugins/kf5/powerdevil/powerdevilupowerbackend.so
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.*
%{_datadir}/knotifications5/powerdevil.notifyrc
%{_libdir}/libexec/kauth/chargethresholdhelper
%{_datadir}/qlogging-categories5/powerdevil.categories
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_datadir}/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
%{_datadir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
%{_prefix}/lib/systemd/user/plasma-powerdevil.service
%{_libdir}/libpowerdevilcore.so.*
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevil*.so
%{_libdir}/qt5/plugins/powerdevil
%{_datadir}/applications/kcm_powerdevil*.desktop
