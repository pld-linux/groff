Summary:	GNU groff text formatting package
Summary(de):	GNU groff-Textformatierungspaket
Summary(fr):	Paquetage de formatage de texte groff de GNU
Summary(pl):	GNU groff - pakiet do formatowania tekstu 
Summary(tr):	GNU groff metin bi�emleme paketi
Name:		groff
Version:	1.11a
Release:	16
Copyright:	GPL
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	troff-to-ps.fpi
Patch0:		%{name}-fhs.patch
Patch1:		%{name}-1.11-safer.patch
Patch2:		%{name}-X11.patch
Patch3:		%{name}-include-opt.patch
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
verarbeitet. Das Paket wird zum Lesen von man-Seiten ben�tigt.

%description -l fr
Le syst�me de formatage de texte groff peut �tre utilis� pour cr�er des
documents d'aspect professionnel sur papier et � l'�cran. Toutes les pages
man sont trait�es avec groff, vous avez donc besoin de ce paquetage pour les
visualiser.

%description -l pl
System formatowania tekstu groff mo�e by� u�ywany do tworzenia
profesjonalnie wygl�daj�cego dokumentu zar�wno na papierze jak i na konsoli.
Wszystkie podr�czniki ekranowe (man) potrzebuj� groff'a do formatowania
tekstu na ekranie. Tak wi�c potrzebujesz tego pakietu do czytania
podr�cznik�w ekranowych.

%description -l tr
groff metin bi�emleme sistemi ka��t veya bilgisayar ekran� �zerinde
profesyonel g�r�n�me sahip belgeler yaratmaya yarar. B�t�n k�lavuz (man)
sayfalar� groff ile haz�rlanm��t�r. man sayfalar�n� okuyabilmek i�in groff
paketine gereksiniminiz olacakt�r.

%package	gxditview
Summary:	GNU groff X previewer
Summary(de):	GNU groff-X-Previewer
Summary(fr):	Le visualiseur de fichier groff de GNU, sous X.
Summary(pl):	Groff pod X'y 
Summary(tr):	GNU groff X g�r�nt�leyici
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie

%description gxditview
The package contains the gxditview program, which can be used to format and
view groff documents in X Windows.  For example, man pages can be read using
gxditview.

%description -l de gxditview
Das Paket enth�lt das gxditview-Programm, das zum Formatieren und Anzeigen
von groff-Dokumenten in X-Windows benutzt wird. So lassen sich
beispielsweise auch die man-Seiten mit gxditview einsehen.

%description -l fr gxditview
Ce paquetage contient le programme gxditview, qui peut servir � formater et
viusaliser les documents groff sous X Window. Les pages peuvent, par
exemple, �tre lues avec gxditview.

%description -l pl gxditview
Pakiet ten zawiera program gxditview, kt�ry pozwoli Ci na formatowanie
dokument�w pod X'ami. Na przyk�ad, do czytania por�cznik�w ekranowych.

%description -l tr gxditview
Bu paket groff belgelerini g�r�nt�leyip de�i�tirmeye yarayan gxditview
program�n� i�erir. �rne�in man sayfalar� gxditview kullan�larak okunabilir.

%prep
%setup -q -n groff-1.11
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
PATH=$PATH:/usr/X11R6/bin
CXX='g++' CC='gcc' CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
LDFLAGS=-s \
./configure %{_target_platform} \
	--prefix=%{_prefix}
make

cd xditview
xmkmf
make 

%install
rm -rf $RPM_BUILD_ROOT
PATH=$PATH:/usr/X11R6/bin

install -d $RPM_BUILD_ROOT%{_libdir}/rhs/rhs-printfilters

make install prefix=$RPM_BUILD_ROOT%{_prefix}

cd xditview
make DESTDIR=$RPM_BUILD_ROOT install install.man 
cd ..

strip $RPM_BUILD_ROOT%{_prefix}/{bin/*,X11R6/bin/*} || :

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

gzip -9fn $RPM_BUILD_ROOT{%{_mandir}/man1/*,/usr/X11R6/man/man1/*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{_datadir}/groff

%attr(755,root,root) %{_bindir}/addftinfo
%attr(755,root,root) %{_bindir}/afmtodit
%attr(755,root,root) %{_bindir}/eqn
%attr(755,root,root) %{_bindir}/geqn
%attr(755,root,root) %{_bindir}/gindxbib
%attr(755,root,root) %{_bindir}/glookbib
%attr(755,root,root) %{_bindir}/gneqn
%attr(755,root,root) %{_bindir}/gnroff
%attr(755,root,root) %{_bindir}/gpic
%attr(755,root,root) %{_bindir}/grefer
%attr(755,root,root) %{_bindir}/grodvi
%attr(755,root,root) %{_bindir}/groff
%attr(755,root,root) %{_bindir}/grog
%attr(755,root,root) %{_bindir}/grolj4
%attr(755,root,root) %{_bindir}/grops
%attr(755,root,root) %{_bindir}/grotty
%attr(755,root,root) %{_bindir}/gsoelim
%attr(755,root,root) %{_bindir}/gtbl
%attr(755,root,root) %{_bindir}/gtroff
%attr(755,root,root) %{_bindir}/hpftodit
%attr(755,root,root) %{_bindir}/indxbib
%attr(755,root,root) %{_bindir}/lkbib
%attr(755,root,root) %{_bindir}/lookbib
%attr(755,root,root) %{_bindir}/neqn
%attr(755,root,root) %{_bindir}/nroff
%attr(755,root,root) %{_bindir}/pfbtops
%attr(755,root,root) %{_bindir}/pic
%attr(755,root,root) %{_bindir}/psbb
%attr(755,root,root) %{_bindir}/refer
%attr(755,root,root) %{_bindir}/soelim
%attr(755,root,root) %{_bindir}/tbl
%attr(755,root,root) %{_bindir}/tfmtodit
%attr(755,root,root) %{_bindir}/troff

%{_mandir}/man1/*

%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/*

%files gxditview
%defattr(644,root,root,755)

%attr(755,root,root) /usr/X11R6/bin/gxditview
%attr(644,root,root) %config /usr/X11R6/lib/X11/app-defaults/GXditview
/usr/X11R6/man/man1/*
