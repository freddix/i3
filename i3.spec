Summary:	Improved tiling WM
Name:		i3
Version:	4.5
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://i3wm.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	9eea2f570ec19affa3ec60b5ab411497
Source1:	i3.target
Source2:	i3wm.service
URL:		http://i3wm.org
BuildRequires:	libev-devel
BuildRequires:	pango-devel
BuildRequires:	pcre-devel
BuildRequires:	startup-notification-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-libXcursor-devel
BuildRequires:	yajl-devel
Requires:	i3status
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
i3 is a tiling window manager, completely written from scratch.
i3 is primarily targeted at advanced users and developers.

%prep
%setup -q

# verbose build
sed -i -e "s|\.SILENT.*||g" common.mk

# use c and ld flags
sed -i -e "s|-O2|%{rpmcflags}|g" common.mk
sed -i -e "s|-Wl,--as-needed|%{rpmldflags}|g" common.mk

%build
%{__make} DEBUG=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/systemd/user

%{__make} DEBUG="" install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/usr/lib/systemd/user

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/i3
%attr(755,root,root) %{_bindir}/i3-config-wizard
%attr(755,root,root) %{_bindir}/i3-dmenu-desktop
%attr(755,root,root) %{_bindir}/i3-dump-log
%attr(755,root,root) %{_bindir}/i3-input
%attr(755,root,root) %{_bindir}/i3-msg
%attr(755,root,root) %{_bindir}/i3-nagbar
%attr(755,root,root) %{_bindir}/i3-sensible-editor
%attr(755,root,root) %{_bindir}/i3-sensible-pager
%attr(755,root,root) %{_bindir}/i3-sensible-terminal
%attr(755,root,root) %{_bindir}/i3bar

%dir %{_sysconfdir}/i3
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/i3/config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/i3/config.keycodes

%{_datadir}/applications/i3.desktop
%{_datadir}/xsessions/i3.desktop

/usr/lib/systemd/user/i3.target
/usr/lib/systemd/user/i3wm.service

