%define		_realname	goats

Summary:	A sticky notes program for GNOME
Summary(pl):	Przyklejane notatki dla GNOME
Name:		gnome-applet-goats
Version:	2.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.menudo.freeserve.co.uk/%{_realname}-%{version}.tar.gz
# Source0-md5:	d2a218fe755f7daa986d232060781793
Patch0:		%{name}-omf.patch
URL:		http://www.menudo.freeserve.co.uk/goats.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-panel-devel >= 2.2.0
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Goats is another post-it note applet for GNOME, modelled after Knotes
for KDE, and also similar to gnome-gnotes. You can create lots of
notes in dayglow colours, type in different fonts, set alarms etc. You
can also run it without the GNOME panel.

%description -l pl
Goats to kolejny aplet z notatkami dla GNOME, wzorowany na Knotes z
KDE, podobny te� do gnome-gnotes. Pozwala tworzy� wiele notatek w
r�nych kolorach, pisa� r�nymi fontami, ustawia� alarmy itp. Mo�e by�
tak�e uruchomiony z panelu GNOME.

%prep
%setup -q -n %{_realname}-%{version}
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-gconf-schema-file-dir=%{_sysconfdir}/gconf/schemas \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{_realname} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun	-p /usr/bin/scrollkeeper-update


%files -f %{_realname}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README TODO
%{_sysconfdir}/gconf/schemas/goats.schemas
%{_libdir}/bonobo/servers/GNOME_GoatsApplet.server
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome-2.0/ui/GNOME_GoatsApplet.xml
%{_pixmapsdir}/*.png
%dir %{_datadir}/goats
%{_datadir}/goats/*
%{_datadir}/sounds/goat_bleat.au
%{_omf_dest_dir}/%{_realname}
