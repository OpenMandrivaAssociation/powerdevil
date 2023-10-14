%define major 5
%define stable %([ "%(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define git 20231014

Name: plasma6-powerdevil
Version: 5.240.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/powerdevil/-/archive/master/powerdevil-master.tar.bz2#/powerdevil-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Summary: KDE 6 Power Saving Tools
URL: http://kde.org/
License: GPL
Group: System/Libraries
Patch2: powerdevil-bump-sonames.patch
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(KF6Activities)
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
BuildRequires: cmake(KF6Wayland)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(LibKWorkspace) >= 5.27.80
BuildRequires: cmake(KF6BluezQt)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(LayerShellQt)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libcap)
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires(meta): power-profiles-daemon
Recommends: plasma6-kinfocenter
Recommends: kf6-networkmanager-qt
Recommends: kf6-bluez-qt

%description
KDE 6 Power Saving Tools.

%prep
%autosetup -p1 -n powerdevil-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html --with-man

%files -f %{name}.lang
%{_datadir}/dbus-1/system.d/*.conf
%{_sysconfdir}/xdg/autostart/powerdevil.desktop
%caps(cap_wake_alarm+ep) %{_libdir}/libexec/org_kde_powerdevil
%{_libdir}/libexec/kf6/kauth/backlighthelper
%{_libdir}/libexec/kf6/kauth/discretegpuhelper
%{_qtdir}/plugins/kf6/powerdevil/powerdevilupowerbackend.so
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.*
%{_datadir}/knotifications6/powerdevil.notifyrc
%{_libdir}/libexec/kf6/kauth/chargethresholdhelper
%{_datadir}/qlogging-categories6/powerdevil.categories
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_datadir}/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
%{_datadir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
%{_prefix}/lib/systemd/user/plasma-powerdevil.service
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevil*.so
%{_qtdir}/plugins/powerdevil
%{_datadir}/applications/kcm_powerdevil*.desktop
%{_libdir}/libpowerdevilconfigcommonprivate.so*
%{_libdir}/libpowerdevilcore.so*
%{_libdir}/libpowerdevilui.so*
%{_prefix}/lib/systemd/user/plasma-powerprofile-osd.service
%{_libdir}/libexec/power_profile_osd_service
%{_datadir}/dbus-1/services/org.kde.powerdevil.powerProfileOsdService.service
