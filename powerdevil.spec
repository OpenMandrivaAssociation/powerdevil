%define major 5
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: powerdevil
Version: 6.5.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/powerdevil/-/archive/%{gitbranch}/powerdevil-%{gitbranchd}.tar.bz2#/powerdevil-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/powerdevil-%{version}.tar.xz
%endif
Summary: KDE 6 Power Saving Tools
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(QCoro6)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(ScreenSaverDBusInterface) >= 5.27.80
BuildRequires: cmake(KF6Screen)
BuildRequires: cmake(Wayland) >= 5.90.0
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(LibKWorkspace) >= 5.27.80
BuildRequires: cmake(KF6BluezQt)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(LayerShellQt)
BuildRequires: cmake(DDCUtil)
BuildRequires: cmake(Plasma)
BuildRequires: cmake(PlasmaQuick)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)
Requires(meta): power-profiles-daemon
Recommends: plasma6-kinfocenter
Recommends: kf6-networkmanager-qt
Recommends: kf6-bluez-qt
# Renamed after 6.0 2025-05-03
%rename plasma6-powerdevil
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE 6 Power Saving Tools.

%files -f %{name}.lang
%{_datadir}/dbus-1/system.d/*.conf
%{_sysconfdir}/xdg/autostart/powerdevil.desktop
%caps(cap_wake_alarm+ep) %{_libdir}/libexec/org_kde_powerdevil
%{_libdir}/libexec/kf6/kauth/backlighthelper
%{_libdir}/libexec/kf6/kauth/discretegpuhelper
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.*
%{_datadir}/knotifications6/powerdevil.notifyrc
%{_libdir}/libexec/kf6/kauth/chargethresholdhelper
%{_datadir}/qlogging-categories6/powerdevil.categories
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_datadir}/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
%{_datadir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
%{_prefix}/lib/systemd/user/plasma-powerdevil.service
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_powerdevilprofilesconfig.so
%{_qtdir}/plugins/powerdevil
%{_datadir}/applications/kcm_powerdevil*.desktop
%{_libdir}/libpowerdevilcore.so*
%{_datadir}/qlogging-categories6/brightness.categories
%{_qtdir}/plugins/kf6/krunner/krunner_powerdevil.so
%{_qtdir}/qml/org/kde/plasma/private/batterymonitor
%{_qtdir}/qml/org/kde/plasma/private/brightnesscontrolplugin
%{_datadir}/qlogging-categories6/batterymonitor.categories
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobile_power.so
%{_datadir}/applications/kcm_mobile_power.desktop
%{_libdir}/libexec/kf6/kauth/wakeupsourcehelper
%{_qtdir}/plugins/plasma/applets/org.kde.plasma.battery.so
%{_qtdir}/plugins/plasma/applets/org.kde.plasma.brightness.so
%{_datadir}/polkit-1/actions/org.kde.powerdevil.wakeupsourcehelper.policy
