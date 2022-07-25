%define debug_package	%{nil}

%define	major	0
%define	libname	%mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Name:		zita-alsa-pcmi
Summary:	Provides easy access to ALSA PCM devices
Version:	0.5.1
Release:	1
License:	GPLv3
Group:		System/Libraries 
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/

BuildRequires:	ecasound-devel

%description
Zita-alsa-pcmi is the successor of clalsadrv. It provides easy access
to ALSA PCM devices, taking care of the many functions required to
open, initialize and use a hw: device in mmap mode, and providing
floating point audio data.

#--------------------------------------------------------------------

%package -n %{libname}
Group:		System/Libraries
Summary:	Libraries for %{name}
Provides:	lib%{name} = %{EVRD}
Obsoletes:	%{_lib}clalsadrv2 < 2.0.1

%description -n	%{libname}
The libraries from %{name} package needed by Aeolus

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develname}
Group:		Development/Other
Summary:	Libraries for %name
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}clalsadrv-devel < 2.0.1

%description -n	%{develname}
Development libraries from %{name}

%files -n %{develname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
sed -i -e '/ldconfig/d' libs/Makefile

%build
cd libs
%make PREFIX=%{buildroot}%{_prefix}

%install
cd libs
%makeinstall PREFIX=%{buildroot}%{_prefix}



