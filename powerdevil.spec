%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: powerdevil
Version: 5.2.1
Release: 1
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
Summary: KDE 5 Power Saving Tools
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5DNSSD)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5IdleTime)
BuildRequires: cmake(ScreenSaverDBusInterface)
BuildRequires: pkgconfig(xrandr)
BuildRequires: ninja
# for kf5_org.freedesktop.ScreenSaver.xml
BuildRequires: plasma-workspace

%description
KDE 5 Power Saving Tools

%libpackage powerdevilconfigcommonprivate 5
%libpackage powerdevilcore 2
%libpackage powerdevilui 5

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches

%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang libpowerdevilcommonconfig
%find_lang powerdevil
%find_lang powerdevilactivitiesconfig
%find_lang powerdevilglobalconfig
%find_lang powerdevilprofilesconfig
cat *.lang >all.lang

%files -f all.lang
%{_sysconfdir}/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
%{_libdir}/libexec/kauth/backlighthelper
%{_libdir}/*.so
%{_libdir}/qt5/plugins/kcm_powerdevil*.so
%{_libdir}/qt5/plugins/kded_powerdevil.so
%{_libdir}/qt5/plugins/powerdevil*.so
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.*
%{_datadir}/knotifications5/powerdevil.notifyrc
%{_datadir}/kservices5/kded/powerdevil.desktop
%{_datadir}/kservices5/powerdevil*.desktop
%{_datadir}/kservicetypes5/powerdevilaction.desktop
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%doc %{_docdir}/HTML/en/kcontrol
