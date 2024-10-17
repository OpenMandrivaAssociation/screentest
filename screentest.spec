Summary: The CRT screen quality testing utility
Name: screentest
Version: 2.0
Release: 4
License: GPLv2
Group: System/X11
Source: http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
URL: https://sourceforge.net/projects/%{name}/
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libglade-2.0)


%description
Screentest is a simple program which displays various patterns
(colors, circles, grids, text) on your screen in order to allow you
to evaluate the quality of your CRT/LCD monitor (sharpness, linearity, etc).

%prep
%setup -q

%build
export LDFLAGS="-lgmodule-2.0"
%configure2_5x
%make

%install
%makeinstall
%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%dir %{_datadir}/%{name}/


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-2mdv2011.0
+ Revision: 614828
- the mass rebuild of 2010.1 packages

* Fri Jan 15 2010 Michael Scherer <misc@mandriva.org> 2.0-1mdv2010.1
+ Revision: 491784
- fix missing directory

  + Peťoš Šafařík <petos@mandriva.org>
    - Documentation like authors, Readme etc. add.
    - Licence fixed
    - Cleaning in SPEC fixed.
    - import screentest


