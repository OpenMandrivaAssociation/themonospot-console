Summary:  Console application to use themonospot (multimedia files parser/editor)
Name:     themonospot-console
Version:  0.1.1
Release:  3
License:  GPLv2
Group:    Video
Source:   http://www.integrazioneweb.com/repository/SOURCES/themonospot-console-%{version}.tar.gz
Url:      http://www.integrazioneweb.com/themonospot

#BuildArch : noarch
%define debug_package %{nil}

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
%makeinstall_std

%files
%doc copying.gpl
%{_libdir}/themonospot/%{name}.exe
%{_bindir}/%{name}
