Summary:	GNU groff text formatting package
Summary(de):	GNU groff-Textformatierungspaket
Summary(fr):	Paquetage de formatage de texte groff de GNU
Summary(pl):	GNU groff - pakiet do formatowania tekstu 
Summary(tr):	GNU groff metin biçemleme paketi
Name:		groff
Version:	1.11.1
Release:	16
Copyright:	GPL
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Source0:	ftp://prep.ai.mit.edu/pub/gnu/groff/%{name}-%{version}.tar.gz
Source1:	troff-to-ps.fpi
Patch0:		groff-fhs.patch
Patch1:		groff-safer.patch
Patch2:		groff-X11.patch
Patch3:		groff-include-opt.patch
Patch4:		groff-DESTDIR.patch
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
Requires:	mktemp
Obsoletes:	groff-tools
Buildroot:	/tmp/%{name}-%{version}-root

%description
The groff text formatting system can be used to create professional looking
documents on both paper and a computer screen.  All the man pages are
processed with groff, so you'll need this package to read man pages.

%description -l de
Das Textformatiersystem groff wird zum Erstellen professioneller Dokumente
auf Papier und Bildschirm verwendet. Alle man-Seiten werden mit groff
verarbeitet. Das Paket wird zum Lesen von man-Seiten benötigt.

%description -l fr
Le système de formatage de texte groff peut être utilisé pour créer des
documents d'aspect professionnel sur papier et à l'écran. Toutes les pages
man sont traitées avec groff, vous avez donc besoin de ce paquetage pour les
visualiser.

%description -l pl
System formatowania tekstu groff mo¿e byæ u¿ywany do tworzenia
profesjonalnie wygl±daj±cego dokumentu zarówno na papierze jak i na konsoli.
Wszystkie podrêczniki ekranowe (man) potrzebuj± groff'a do formatowania
tekstu na ekranie. Tak wiêc potrzebujesz tego pakietu do czytania
podrêczników ekranowych.

%description -l tr
groff metin biçemleme sistemi kaðýt veya bilgisayar ekraný üzerinde
profesyonel görünüme sahip belgeler yaratmaya yarar. Bütün kýlavuz (man)
sayfalarý groff ile hazýrlanmýþtýr. man sayfalarýný okuyabilmek için groff
paketine gereksiniminiz olacaktýr.

%package gxditview
Summary:	GNU groff X previewer
Summary(de):	GNU groff-X-Previewer
Summary(fr):	Le visualiseur de fichier groff de GNU, sous X.
Summary(pl):	Groff pod X'y 
Summary(tr):	GNU groff X görüntüleyici
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie

%description gxditview
The package contains the gxditview program, which can be used to format and
view groff documents in X Windows.  For example, man pages can be read using
gxditview.

%description -l de gxditview
Das Paket enthält das gxditview-Programm, das zum Formatieren und Anzeigen
von groff-Dokumenten in X-Windows benutzt wird. So lassen sich
beispielsweise auch die man-Seiten mit gxditview einsehen.

%description -l fr gxditview
Ce paquetage contient le programme gxditview, qui peut servir à formater et
viusaliser les documents groff sous X Window. Les pages peuvent, par
exemple, être lues avec gxditview.

%description -l pl gxditview
Pakiet ten zawiera program gxditview, który pozwoli Ci na formatowanie
dokumentów pod X'ami. Na przyk³ad, do czytania porêczników ekranowych.

%description -l tr gxditview
Bu paket groff belgelerini görüntüleyip deðiþtirmeye yarayan gxditview
programýný içerir. Örneðin man sayfalarý gxditview kullanýlarak okunabilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
PATH=$PATH:/usr/X11R6/bin
autoconf
CXX="g++"
CC="gcc"
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
LDFLAGS="-s"
export CXX CC CXXFLAGS LDFLAGS
%configure
make

cd xditview
xmkmf
make 

%install
rm -rf $RPM_BUILD_ROOT
PATH=$PATH:/usr/X11R6/bin

install -d $RPM_BUILD_ROOT%{_libdir}/rhs/rhs-printfilters

make install DESTDIR=$RPM_BUILD_ROOT

cd xditview
make DESTDIR=$RPM_BUILD_ROOT install install.man 
cd ..

strip $RPM_BUILD_ROOT{%{_bindir}/*,/usr/X11R6/bin/*} || :

ln -s tmac.s	$RPM_BUILD_ROOT%{_datadir}/groff/tmac/tmac.gs
ln -s tmac.mse  $RPM_BUILD_ROOT%{_datadir}/groff/tmac/tmac.gmse
ln -s tmac.m	$RPM_BUILD_ROOT%{_datadir}/groff/tmac/tmac.gm
ln -s eqn	$RPM_BUILD_ROOT%{_bindir}/geqn
ln -s indxbib	$RPM_BUILD_ROOT%{_bindir}/gindxbib
ln -s lookbib	$RPM_BUILD_ROOT%{_bindir}/glookbib
ln -s neqn	$RPM_BUILD_ROOT%{_bindir}/gneqn
ln -s nroff	$RPM_BUILD_ROOT%{_bindir}/gnroff
ln -s troff	$RPM_BUILD_ROOT%{_bindir}/gtroff
ln -s tbl	$RPM_BUILD_ROOT%{_bindir}/gtbl
ln -s pic	$RPM_BUILD_ROOT%{_bindir}/gpic
ln -s refer	$RPM_BUILD_ROOT%{_bindir}/grefer
ln -s soelim	$RPM_BUILD_ROOT%{_bindir}/gsoelim

echo ".so eqn.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/geqn.1
echo ".so indxbib.1" > $RPM_BUILD_ROOT%{_mandir}/man1/gindxbib.1
echo ".so lookbib.1" > $RPM_BUILD_ROOT%{_mandir}/man1/glookbib.1
echo ".so neqn.1" >    $RPM_BUILD_ROOT%{_mandir}/man1/gneqn.1
echo ".so nroff.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/gnroff.1
echo ".so pic.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/gpic.1
echo ".so refer.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/grefer.1
echo ".so soelim.1" >  $RPM_BUILD_ROOT%{_mandir}/man1/gsoelim.1
echo ".so tbl.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/gtbl.1
echo ".so troff.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/gtroff.1

install $RPM_SOURCE_DIR/troff-to-ps.fpi \
	$RPM_BUILD_ROOT%{_libdir}/rhs/rhs-printfilters

gzip -9fn $RPM_BUILD_ROOT{%{_mandir}/man1/*,/usr/X11R6/man/man1/*} \
	NEWS PROBLEMS PROJECTS README TODO BUG-REPORT ChangeLog \
	xditview/{ChangeLog,README,TODO}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,PROBLEMS,PROJECTS,README,TODO,BUG-REPORT,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/*

%{_datadir}/groff
%{_mandir}/man1/*

%files gxditview
%defattr(644,root,root,755)
%doc xditview/{ChangeLog,README,TODO}.gz
%attr(755,root,root) /usr/X11R6/bin/gxditview

%attr(644,root,root) %config /usr/X11R6/lib/X11/app-defaults/GXditview
/usr/X11R6/man/man1/*
