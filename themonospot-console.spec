Summary   : Console application to use themonospot (multimedia files parser/editor)
Name      : themonospot-console
Version   : 0.1.1
Release   : %mkrel 1
License   : GPLv2
Group     : Video
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-console-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL       : http://www.integrazioneweb.com/themonospot

#BuildArch : noarch

BuildRequires: mono-devel
BuildRequires: themonospot-base-devel


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
%doc copying.gpl
%{_libdir}/themonospot/%{name}.exe
%{_bindir}/%{name}




%changelog
* Sat Jan 02 2010 Armando Basile <hman@mandriva.org> 0.1.1-1mdv2010.1
+ Revision: 485128
- removed GAC use

* Thu Dec 24 2009 Armando Basile <hman@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 482033
- first public release of console application for new Themonospot suite
- create themonospot-console

