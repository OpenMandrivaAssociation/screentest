Summary: The CRT screen quality testing utility
Name: screentest
Version: 2.0
Release: %mkrel 1
License: GPL
Group: System/X11
Source: http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
URL: http://sourceforge.net/projects/%{name}/
BuildRequires: gtk+2-devel
BuildRequires: libglade2-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Screentest is a simple program which displays various patterns
(colors, circles, grids, text) on your screen in order to allow you
to evaluate the quality of your CRT/LCD monitor (sharpness, linearity, etc).

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall
%find_lang %{name}


%files -f %{name}.lang
%defattr(-, root,root)
%doc README NEW_TESTS COPYING ChangeLog INSTALL NEWS AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.glade

