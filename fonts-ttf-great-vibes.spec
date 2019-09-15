%define pkgname great-vibes

Summary:	Great Vibes font family
Name:		fonts-ttf-great-vibes
Version:	20190915
Release:	1
License:	SIL Open Font License
Group:		System/Fonts/True type
URL:		https://www.fontsquirrel.com/fonts/great-vibes
Source0:	https://www.fontsquirrel.com/fonts/download/great-vibes/%{pkgname}.zip
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
The "Great Vibes" typeface is a curly calligraphic font.

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
%__mkdir_p %{buildroot}%{_xfontdir}/OTF/%{pkgname}

%__install -m 644 *.otf %{buildroot}%{_xfontdir}/OTF/%{pkgname}
ttmkfdir %{buildroot}%{_xfontdir}/OTF/%{pkgname} -o %{buildroot}%{_xfontdir}/OTF/%{pkgname}/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/OTF/%{pkgname}/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/%{pkgname} \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-%{pkgname}:pri=50

%__install -d %{buildroot}%{_docdir}/%{name}

%files
%dir %{_xfontdir}/OTF/%{pkgname}
%{_xfontdir}/OTF/%{pkgname}/*.otf
%verify(not mtime) %{_datadir}/fonts/OTF/%{pkgname}/fonts.dir
%{_xfontdir}/OTF/%{pkgname}/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-%{pkgname}:pri=50
