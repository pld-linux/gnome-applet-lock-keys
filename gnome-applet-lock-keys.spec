%define		_realname	lock-keys-applet
Summary:	Show status of your lock key leds
Summary(pl):	Pokazuje status diod klawiatury
Name:		gnome-applet-lock-keys
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.wh-hms.uni-ulm.de/~mfcn/shared/lock-keys/%{_realname}-%{version}.tar.gz
# Source0-md5:	8dc772d62f0881c8978513d7e69de3db
URL:		http://mfcn.ilo.de/led_applet/
BuildRequires:	gnome-desktop-devel >= 2.2.0
BuildRequires:	gnome-panel-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.2.0
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lock keys applet is a gnome2 applet, that shows the status of the
CAPS-, NUM- and SCROLL-Lock keys of your keyboard. This isn't
especially usefull for normal keyboards, as they got leds for that.
But some keyboards (especially wireless keyboards) don't have. One
more feature of the applet is that it saves the status of the
lock-keys and restores it, when starting gnome2.

%description -l pl
Lock keys applet jest appletem gnome2, który pokazuje stan diod
CAPS-, NUM- i SCROLL-Lock klawiatury. Nie jest mo¿e u¿yteczny podczas
korzystania z normalnej klawiatury, gdy¿ posiadaj± one te diody.
Jednak niektóre klawiatury (g³ównie bezprzewodowe) nie posiadaj± tych
diod. Dodatkowym u³atwienie apletu jest to, ¿e zapamiêtuje on stan
tych klawiszy i odtwarza go przy uruchamianiu gnome2.

%prep
%setup -q -n %{_realname}-%{version}

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir=%{_datadir}/locale

%find_lang lock-keys-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f lock-keys-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lock-keys-applet
%{_libdir}/bonobo/servers/*.server
%{_datadir}/omf/lock-keys-applet/*.omf
%{_pixmapsdir}/*.png
