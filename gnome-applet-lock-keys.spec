%define		_realname	lock-keys-applet
Summary:	Show status of your lock key leds
Summary(pl.UTF-8):	Pokazuje status diod klawiatury
Name:		gnome-applet-lock-keys
Version:	1.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://www.wh-hms.uni-ulm.de/~mfcn/shared/lock-keys/%{_realname}-%{version}.tar.gz
# Source0-md5:	8dc772d62f0881c8978513d7e69de3db
URL:		http://mfcn.ilo.de/led_applet/
BuildRequires:	gnome-desktop-devel >= 2.2.0
BuildRequires:	gnome-panel-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	rpmbuild(macros) >= 1.71
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lock keys applet is a GNOME 2 applet, that shows the status of the
CAPS-, NUM- and SCROLL-Lock keys of your keyboard. This isn't
especially usefull for normal keyboards, as they got leds for that.
But some keyboards (especially wireless keyboards) don't have. One
more feature of the applet is that it saves the status of the
lock-keys and restores it, when starting GNOME 2.

%description -l pl.UTF-8
Lock keys applet jest appletem GNOME 2, który pokazuje stan diod
CAPS-, NUM- i SCROLL-Lock klawiatury. Nie jest może użyteczny podczas
korzystania z normalnej klawiatury, gdyż posiadają one te diody.
Jednak niektóre klawiatury (głównie bezprzewodowe) nie posiadają tych
diod. Dodatkowym ułatwienie apletu jest to, że zapamiętuje on stan
tych klawiszy i odtwarza go przy uruchamianiu GNOME 2.

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
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f lock-keys-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lock-keys-applet
%{_libdir}/bonobo/servers/GNOME_LockKeysApplet.server
%dir %{_omf_dest_dir}/lock-keys-applet
%{_omf_dest_dir}/lock-keys-applet/lock-keys-applet-C.omf
%lang(de) %{_omf_dest_dir}/lock-keys-applet/lock-keys-applet-de.omf
%{_pixmapsdir}/lock-keys-applet.png
