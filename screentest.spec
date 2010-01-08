Summary: The CRT screen quality testing utility
Name: screentest
Version: 2.0
Release: %mkrel 1
License: GPLv2
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
%__rm -rf "%{buildroot}"

%makeinstall
%find_lang %{name}

%clean
%__rm -rf "%{buildroot}"

%files -f %{name}.lang
%defattr(-, root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.glade

