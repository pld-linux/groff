Summary:     GNU groff text formatting package
Summary(de): GNU groff-Textformatierungspaket
Summary(fr): Paquetage de formatage de texte groff de GNU
Summary(pl): GNU groff - pakiet do formatowania tekstu 
Summary(tr): GNU groff metin bi�emleme paketi
Name:        groff
Version:     1.11a
Release:     9
Copyright:   GPL
Group:       Applications/Publishing
Source0:     ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:     troff-to-ps.fpi
Patch:       groff-1.11-make.patch
Patch1:      groff-1.11-safer.patch
Patch2:      groff-1.11-bash2.patch
Requires:    mktemp
Buildroot:   /tmp/%{name}-%{version}-root
Obsoletes:   groff-tools

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

%package gxditview
Summary:     GNU groff X previewer
Summary(de): GNU groff-X-Previewer
Summary(fr): Le visualiseur de fichier groff de GNU, sous X.
Summary(pl): Groff pod X'y 
Summary(tr): GNU groff X g�r�nt�leyici
Group:       Applications/Publishing

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
%patch -p1
%patch1 -p1

%build
PATH=$PATH:/usr/X11R6/bin
CXX='g++' CC='gcc' CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr
make
cd xditview
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
PATH=$PATH:/usr/X11R6/bin
install -d $RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters

make install prefix=$RPM_BUILD_ROOT/usr
cd xditview
make DESTDIR=$RPM_BUILD_ROOT install install.man
strip $RPM_BUILD_ROOT/usr/bin/* || :

ln -s tmac.s	$RPM_BUILD_ROOT/usr/lib/groff/tmac/tmac.gs
ln -s tmac.mse $RPM_BUILD_ROOT/usr/lib/groff/tmac/tmac.gmse
ln -s tmac.m	$RPM_BUILD_ROOT/usr/lib/groff/tmac/tmac.gm
ln -s eqn	$RPM_BUILD_ROOT/usr/bin/geqn
ln -s indxbib	$RPM_BUILD_ROOT/usr/bin/gindxbib
ln -s lookbib	$RPM_BUILD_ROOT/usr/bin/glookbib
ln -s neqn	$RPM_BUILD_ROOT/usr/bin/gneqn
ln -s nroff	$RPM_BUILD_ROOT/usr/bin/gnroff
ln -s troff	$RPM_BUILD_ROOT/usr/bin/gtroff
ln -s tbl	$RPM_BUILD_ROOT/usr/bin/gtbl
ln -s pic	$RPM_BUILD_ROOT/usr/bin/gpic
ln -s refer	$RPM_BUILD_ROOT/usr/bin/grefer
ln -s soelim	$RPM_BUILD_ROOT/usr/bin/gsoelim

echo ".so eqn.1" >     $RPM_BUILD_ROOT/usr/man/man1/geqn.1
echo ".so indxbib.1" > $RPM_BUILD_ROOT/usr/man/man1/gindxbib.1
echo ".so lookbib.1" > $RPM_BUILD_ROOT/usr/man/man1/glookbib.1
echo ".so neqn.1" >    $RPM_BUILD_ROOT/usr/man/man1/gneqn.1
echo ".so nroff.1" >   $RPM_BUILD_ROOT/usr/man/man1/gnroff.1
echo ".so pic.1" >     $RPM_BUILD_ROOT/usr/man/man1/gpic.1
echo ".so refer.1" >   $RPM_BUILD_ROOT/usr/man/man1/grefer.1
echo ".so soelim.1" >  $RPM_BUILD_ROOT/usr/man/man1/gsoelim.1
echo ".so tbl.1" >     $RPM_BUILD_ROOT/usr/man/man1/gtbl.1
echo ".so troff.1" >   $RPM_BUILD_ROOT/usr/man/man1/gtroff.1

install $RPM_SOURCE_DIR/troff-to-ps.fpi $RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
/usr/lib/groff
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
%attr(755, root, root) /usr/lib/rhs/rhs-printfilters/*

%files gxditview
%attr(755, root, root) /usr/X11R6/bin/gxditview
%attr(644, root, root) %config /usr/X11R6/lib/X11/app-defaults/GXditview
%attr(644, root,  man) /usr/X11R6/man/man1/gxditview.1x

%changelog
* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- fix makefiles to work with bash2

* Thu Sep  8 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.11a-8]
- some man page is now maked as nroff include instead
  making sym link (this allow compress man pages in future).

* Mon Jun 29 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.11a-7]
- added pl translation,
- added %defattr support,
- build from non root's account.

* Mon Jun 29 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- build agains glibc-2.1

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use g++ for C++ code

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- manhattan and buildroot

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- made xdefaults file a config file

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- split perl components into separate subpackage

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated to 1.11a
- added safe troff-to-ps.fpi

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- removed troff-to-ps.fpi for security reasons.

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc
