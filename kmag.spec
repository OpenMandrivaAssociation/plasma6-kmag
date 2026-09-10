#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Screen magnifier for KDE Plasma
Name:		kmag
Version:	26.08.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/applications/utilities/kmag/
%if 0%{?git:1}
Source0:	https://invent.kde.org/accessibility/kmag/-/archive/%{gitbranch}/kmag-%{gitbranchd}.tar.bz2#/kmag-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kmag-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(QAccessibilityClient)
BuildRequires:	cmake(KF6DocTools)

%rename plasma6-kmag

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KMag is a small utility for Linux to magnify a part of the screen. KMag is very
useful for people with visual disabilities and for those working in the fields
of image analysis, web development etc.

%files -f %{name}.lang
%{_bindir}/kmag
%{_iconsdir}/hicolor/*/*/kmag*
%{_datadir}/applications/org.kde.kmag.desktop
%{_datadir}/kmag/icons/*/*/*/*
%{_mandir}/man1/kmag.1*
%{_datadir}/metainfo/org.kde.kmag.metainfo.xml
