Name:           libspiro
Version:        20071029
Release:        3.1%{?dist}
Summary:        Library to simplify the drawing of beautiful curves

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://libspiro.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_src-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This library will take an array of spiro control points and 
convert them into a series of bézier splines which can then 
be used in the myriad of ways the world has come to use béziers. 

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n libspiro-20071029

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README gpl.txt README-RaphLevien
%{_libdir}/*.so.*

%files devel
%doc README gpl.txt README-RaphLevien
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20071029-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Kevin Fenzi <kevin@tummy.com> - 20071029-1
- Initial version for Fedora
