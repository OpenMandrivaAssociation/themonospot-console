Summary   : Console application to use themonospot (multimedia files parser/editor)
Name      : themonospot-console
Version   : 0.1.0
Release   : %mkrel 1
License   : GPLv2
Group     : Video
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-console-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL       : http://www.integrazioneweb.com/themonospot

#BuildArch : noarch

BuildRequires: mono >= 1.2.3
BuildRequires: pkgconfig
BuildRequires: themonospot-base >= 0.8.1

Requires: mono >= 1.2.3
Requires: themonospot-base >= 0.8.1

%description
themonospot-console is a mono console application to scan multimedia files
using themonospot base component and his plugins. 


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_libdir}/%{name}/
%{_bindir}/%{name}/

%changelog
* Mon Dec 14 2009 Armando Basile <hmandevteam@gmail.com> 0.1.0-1mdv2010.1
- first release of new console application to use themonospot
