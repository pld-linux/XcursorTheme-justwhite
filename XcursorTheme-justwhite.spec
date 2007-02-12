%define		_name justwhite
Summary:	X11 cursor theme - justwhite
Summary(pl.UTF-8):   Notyw kursorów dla X11 - justwhite
Name:		XcursorTheme-%{_name}
Version:	0.2
Release:	1
License:	Artistic 2.0
Group:		Themes
Source0:	http://www.kde-look.org/content/files/10394-%{_name}-%{version}.tar.bz2
# Source0-md5:	41808fac6bafc7f6adb6ce6910166952
URL:		http://www.kde-look.org/content/show.php?content=10394
BuildRequires:	XFree86 >= 4.3
BuildArch:	noarch
Requires:	XFree86 >= 4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A gradiented, white/gray cursor theme.

%description -l pl.UTF-8
Szaro-biały motyw kursorów z gradientem.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}
%{__tar} xfj %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}/
mv -f  $RPM_BUILD_ROOT%{_iconsdir}/%{_name}{-%{version},}
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/{*.sh,sshot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}
