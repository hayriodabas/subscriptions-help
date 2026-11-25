#!/usr/bin/env python3
"""Builds Subscriptions' standalone 12-locale Help & Privacy static site (Transit Line palette)."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_URL = "https://hayriodabas.github.io/subscriptions-help"
CONTACT_EMAIL = "hayriodabas@gmail.com"
UPDATED = "2026-11-25"

CSS = """\
:root {
  color-scheme: light dark;
  --paper: #f3f2ee;
  --card: #ffffff;
  --inset: #e8e6e0;
  --rule: #d5d2c9;
  --ink: #17191d;
  --ink-muted: #5a5e66;
  --line-track: #24262b;
  --accent: #e8562a;
  --accent-link: #b93a14;
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #141518;
    --card: #1d1f24;
    --inset: #25282f;
    --rule: #343740;
    --ink: #f3f2ee;
    --ink-muted: #a1a5ae;
    --line-track: #f3f2ee;
    --accent: #e8562a;
    --accent-link: #ff7a52;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font: 16.5px/1.64 -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
.route-header {
  height: 12px;
  background: linear-gradient(90deg, var(--line-track) 0 72%, var(--accent) 72% 100%);
}
main {
  max-width: 780px;
  margin: 0 auto;
  padding: 36px 20px 72px;
}
.hero {
  display: flex;
  align-items: center;
  gap: 18px;
  margin-bottom: 18px;
}
.hero img {
  width: 68px;
  height: 68px;
  border-radius: 16px;
  flex-shrink: 0;
  border: 1px solid var(--rule);
}
.eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--accent-link);
}
h1 {
  font-size: 34px;
  line-height: 1.1;
  font-weight: 750;
  margin: 4px 0 4px;
  letter-spacing: -0.02em;
}
.lede {
  font-size: 17.5px;
  color: var(--ink-muted);
  margin: 0 0 22px;
}
nav.primary-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 20px;
  padding: 12px 0;
  border-top: 1px solid var(--rule);
  border-bottom: 1px solid var(--rule);
  margin-bottom: 16px;
  font-size: 14.5px;
  font-weight: 600;
}
.lang-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin: 0 0 28px;
}
.lang-chip {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  border: 1px solid var(--rule);
  background: var(--card);
  font-size: 13px;
  text-decoration: none;
  color: var(--ink);
}
.lang-chip.current {
  background: var(--accent);
  border-color: var(--accent);
  color: #ffffff;
  font-weight: 600;
}
a {
  color: var(--accent-link);
  text-decoration-thickness: 1.5px;
  text-underline-offset: 3px;
}
h2 {
  font-size: 21px;
  line-height: 1.25;
  margin: 34px 0 12px;
  font-weight: 700;
}
.stops {
  position: relative;
  margin: 12px 0 0 8px;
  padding-left: 26px;
  border-left: 3px solid var(--line-track);
  list-style: none;
}
.stops li {
  position: relative;
  margin: 0 0 14px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 10px;
  padding: 14px 16px;
}
.stops li::before {
  content: "";
  position: absolute;
  left: -34px;
  top: 18px;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--card);
  border: 3px solid var(--line-track);
}
.stops li:last-child::before {
  background: var(--accent);
  border-color: var(--accent);
}
.stops li strong {
  display: block;
  margin-bottom: 4px;
  font-size: 16px;
}
.faq-card {
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 10px;
  padding: 14px 17px;
  margin: 10px 0;
}
.faq-card h3 {
  font-size: 16.5px;
  line-height: 1.3;
  margin: 0 0 6px;
  font-weight: 650;
}
.faq-card p {
  margin: 0;
  color: var(--ink);
}
table.fact-table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 10px;
  overflow: hidden;
}
.fact-table th, .fact-table td {
  text-align: left;
  padding: 11px 14px;
  border-bottom: 1px solid var(--rule);
  font-size: 15px;
  vertical-align: top;
}
.fact-table th {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--ink-muted);
  background: var(--inset);
}
.fact-table tr:last-child td { border-bottom: none; }
.locale-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(215px, 1fr));
  gap: 10px;
  list-style: none;
  padding: 0;
}
.locale-grid li {
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 10px;
  padding: 12px 14px;
}
.privacy-block {
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 10px;
  padding: 15px 17px;
  margin: 10px 0;
}
.privacy-block h2 {
  margin: 0 0 6px;
  font-size: 17.5px;
}
.privacy-block p {
  margin: 0;
}
footer {
  margin-top: 46px;
  padding-top: 16px;
  border-top: 1px solid var(--rule);
  color: var(--ink-muted);
  font-size: 14px;
}
@media (max-width: 560px) {
  h1 { font-size: 28px; }
  main { padding: 26px 16px 54px; }
  .hero img { width: 56px; height: 56px; }
}
"""

LOCALES = {
    "en-US": {
        "name": "English",
        "html_lang": "en",
        "app": "Subscriptions",
        "subtitle": "Renewal Tracker",
        "nav_help": "Help",
        "nav_privacy": "Privacy Policy",
        "nav_langs": "All languages",
        "contact_title": "Support & Contact",
        "contact_body": f"Questions, bug reports or feedback for Subscriptions: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Updated {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "Help & Guide",
            "lede": "What leaves before payday: a chronological charge line built from the prices and dates you enter.",
            "steps_title": "How it works",
            "steps": [
                ("Enter what recurs", "Tap + and add a name, price, currency, billing rhythm (every N days, weeks, months or years), first payment date, category, card and how many people share it. Turn on Free trial and set its end date when a trial starts first."),
                ("Read the Line and payday split", "The Line tab orders upcoming charges by day with a running total. Set your payday under Settings > Payday and the line splits at every payday so you can see what leaves before the next cheque."),
                ("Handle announced price rises and one-off charges", "Inside any subscription, tap A price change is coming to schedule a future rate from a specific date without changing earlier charges. Long-press a charge on the Line or tap the menu on a charge row to skip it or record a one-time amount."),
                ("Review, pause, cancel and save", "Pause a service with Put on hold to stop upcoming charges and alerts until Back on. Mark cancelled services as ended to tally Saved by cancelling on the Year tab, or run Start the check-up to review active plans from highest yearly cost downward.")
            ],
            "faq_title": "Questions & Answers",
            "faqs": [
                ("Does Subscriptions cancel services for me?", "No. Subscriptions does not link to providers or terminate accounts on your behalf. Cancel directly with the service, then tap Mark as cancelled in the app and record a cancellation link inside Notes if helpful."),
                ("Does it connect to my bank or scan my emails?", "No. Subscriptions reads nothing from bank accounts, cards, inboxes or the App Store. Every entry stays local and reflects only what you type in."),
                ("How are multiple currencies counted?", "Each currency keeps its own separate total across the Line and the Year tab. The app does not perform automatic currency conversion."),
                ("How do totals and widgets update?", "Tapping How it is counted in Settings explains real charge dates, monthly/yearly averages, month-end clamping, holds and split shares. Home Screen and Lock Screen widgets refresh automatically at midnight and whenever you edit your list."),
                ("What is included free, and what unlocks with Pro?", "Up to 5 subscriptions, the Line, payday splits, price changes, single-charge edits, Heads-up alerts, Check-up, savings tracking, widgets, JSON backup files and Siri questions are free. Subscriptions Pro is a one-time in-app purchase for unlimited subscriptions, local charge/trial reminders, the 12-month Year chart with category/card breakdowns and CSV export."),
                ("How do I move my list or get a refund?", "Use Settings > Save a backup file and Restore from a backup on a new iPhone. Use Settings > Restore Purchase if you switched devices after buying Pro. Refunds for App Store purchases are processed by Apple at reportaproblem.apple.com.")
            ]
        },
        "privacy": {
            "title": "Privacy Policy",
            "lede": "Your subscription list belongs strictly on your device. No account, no analytics and no servers.",
            "summary_title": "Summary",
            "rows": [
                ("Data collected by us", "None"),
                ("Accounts & sign-in", "None required"),
                ("Bank or email linking", "None"),
                ("Ads & third-party SDKs", "None"),
                ("Storage", "On-device private storage & local widget container only"),
                ("Delete all data", "Settings > Delete all subscriptions, or remove the app")
            ],
            "sections": [
                ("On-device storage and widget", "Subscriptions writes your list to a local file inside your iPhone app storage and a local shared container so your Home Screen and Lock Screen widgets can show upcoming charges without network access. Preferences such as reminder hour, payday schedule and currency filters stay in local UserDefaults."),
                ("Notifications and Siri", "When you enable reminders, notifications are scheduled locally on your device using iOS UserNotifications based on the dates in your list. Siri Shortcuts answer questions about next renewals and monthly totals locally using on-device data."),
                ("In-app purchase", "Subscriptions Pro is offered as a single non-consumable in-app purchase processed exclusively by Apple through StoreKit 2. We never receive your payment method, billing address or Apple ID."),
                ("Backups and CSV export", "When you tap Save a backup file or Export as CSV, iOS lets you save or share that file directly via Files, AirDrop or Mail. Neither file leaves your device unless you choose where to send it."),
                ("Changes and contact", "If this policy is updated for a future version of Subscriptions, the revision date and notes appear on this page.")
            ]
        }
    },
    "tr": {
        "name": "Türkçe",
        "html_lang": "tr",
        "app": "Abonelikler",
        "subtitle": "Ödeme Akışı Takibi",
        "nav_help": "Yardım",
        "nav_privacy": "Gizlilik Politikası",
        "nav_langs": "Tüm diller",
        "contact_title": "Destek ve İletişim",
        "contact_body": f"Abonelikler hakkında soru ve hata bildirimleri için: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Güncelleme {UPDATED} · Abonelikler (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "Yardım ve Kılavuz",
            "lede": "Maaş gününe kadar ne çıkıyor: girdiğin fiyat ve tarihlere göre gün gün sıralanan ödeme akışı.",
            "steps_title": "Nasıl kullanılır",
            "steps": [
                ("Düzenli ödemelerini ekle", "+ düğmesine dokunup ad, fiyat, para birimi, yinelenme sıklığı, ilk ödeme günü, kategori, kart ve paylaşan kişi sayısını gir. Deneme süresi varsa Ücretsiz deneme seçeneğini aç."),
                ("Akış ve maaş günü ayrımı", "Akış sekmesi yaklaşan ödemeleri güne göre dizer ve toplamı gösterir. Ayarlar > Maaş günü kısmından maaş gününü seçersen akış her maaş gününde bölünür."),
                ("Duyurulan zam ve tek seferlik tutarlar", "Bir aboneliğin sayfasında Fiyat değişecek seçerek gelecek bir tarihten geçerli olacak yeni fiyatı ekle. Akışta veya detayda bir ödemeye basılı tutarak ya da menüsünden yalnız o ödemeyi atlayabilir veya farklı tutar girebilirsin."),
                ("Beklemeye al, gözden geçir, iptal et", "Bir hizmeti geçici durdurmak için Beklemeye al kullan. Sağlayıcıda iptal ettikten sonra İptal edildi olarak işaretle dediğinde Yıl sekmesi tasarruf toplamını hesaplar. Gözden geçirme en pahalıdan başlayarak tek tek karar vermeni sağlar.")
            ],
            "faq_title": "Sık Sorulan Sorular",
            "faqs": [
                ("Uygulama aboneliğimi otomatik iptal eder mi?", "Hayır. Abonelikler bankaya veya sağlayıcıya bağlanmaz; sağlayıcının kendi sitesinden ya da Apple Abonelikler'den iptal ettikten sonra uygulamada İptal edildi olarak işaretle."),
                ("Banka veya e-posta bağlantısı gerekiyor mu?", "Hayır. Uygulama hesap, banka bağlantısı veya e-posta izni istemez; yalnızca senin yazdığın kayıtları tutar."),
                ("Farklı para birimleri nasıl toplanır?", "Her para birimi kendi ayrı toplamını tutar. İnternetten döviz kuru çekilmez ve kurlar otomatik çevrilmez."),
                ("Rakamların hesabı ve araç takımı nasıl çalışır?", "Ayarlar > Nasıl hesaplanır sayfası her hesabı adım adım açıklar. Ana ekran ve kilit ekranı araç takımı listeni değiştirdiğinde ve gece yarısı otomatik güncellenir."),
                ("Ücretsiz sürüm ve Pro farkı nedir?", "5 aboneliğe kadar akış, maaş günü ayrımı, fiyat değişikliği, tek seferlik tutar notları, Haberin olsun uyarıları, Gözden geçirme, araç takımı, yedek dosyası ve Siri yanıtları ücretsizdir. Abonelikler Pro tek seferlik ödemedir; sınırsız abonelik, yerel bildirimler, Yıl grafikleri ve CSV dışa aktarma açar."),
                ("Yeni iPhone'a taşıma, satın almayı geri yükleme ve iade", "Ayarlar > Yedek dosyası kaydet ve Yedekten geri yükle ile listeni taşıyabilirsin. Yeni cihazda Ayarlar > Satın almayı geri yükle dokun. İade talepleri Apple üzerinden reportaproblem.apple.com adresinden yapılır.")
            ]
        },
        "privacy": {
            "title": "Gizlilik Politikası",
            "lede": "Abonelik listen yalnızca kendi iPhone'unda durur. Hesap yok, takip yok, sunucu yok.",
            "summary_title": "Özet",
            "rows": [
                ("Tarafımızca toplanan veri", "Hiçbiri"),
                ("Hesap veya giriş", "Gerekmez"),
                ("Banka veya e-posta erişimi", "Yok"),
                ("Reklam ve analiz SDK'sı", "Yok"),
                ("Depolama", "Yalnızca cihazdaki özel depolama ve yerel araç takımı alanı"),
                ("Tüm veriyi silme", "Ayarlar > Tüm abonelikleri sil veya uygulamayı kaldırma")
            ],
            "sections": [
                ("Cihaz içi depolama ve araç takımı", "Listen iPhone'unun özel uygulama klasöründe tek bir dosya olarak saklanır; ana ekran ve kilit ekranı araç takımının internet gerektirmeden çalışabilmesi için cihaz içindeki yerel paylaşılan alanda anlık özet tutulur."),
                ("Bildirimler ve Siri", "Hatırlatıcıları açtığında bildirimler tamamen iPhone içinde yerel olarak planlanır. Siri kısayolları veriyi dışarı göndermeden yerel listeden yanıt verir."),
                ("Uygulama içi satın alma", "Abonelikler Pro tek seferlik tüketilemeyen bir satın almadır ve Apple StoreKit 2 üzerinden işlenir; ödeme bilgilerin bize ulaşmaz."),
                ("Yedek dosyası ve CSV dışa aktarma", "Yedek dosyası kaydet veya CSV dışa aktar seçtiğinde iOS paylaşım ekranından dosyayı nereye kaydedeceğini yalnızca sen seçersin."),
                ("Değişiklikler", "Gelecekteki sürümlerde değişiklik olursa güncelleme tarihi bu sayfada yayımlanır.")
            ]
        }
    },
    "de-DE": {
        "name": "Deutsch",
        "html_lang": "de",
        "app": "Abo Manager",
        "subtitle": "Zahlungsverlauf & Zahltag",
        "nav_help": "Hilfe",
        "nav_privacy": "Datenschutz",
        "nav_langs": "Alle Sprachen",
        "contact_title": "Kontakt & Support",
        "contact_body": f"Fragen oder Hinweise zu Abo Manager: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Stand {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "Hilfe & Anleitung",
            "lede": "Was vor dem Zahltag abgeht: jede Abbuchung an ihrem Tag entlang eines übersichtlichen Zeitstrahls.",
            "steps_title": "So funktioniert es",
            "steps": [
                ("Abos manuell eintragen", "Tippe auf + und ergänze Name, Betrag, Währung, Rhythmus, erste Zahlung, Kategorie, Karte und geteilte Personen. Bei einer Testphase aktivierst du das Enddatum."),
                ("Zeitstrahl und Zahltag nutzen", "Im Tab Zeitstrahl stehen alle kommenden Abbuchungen chronologisch mit laufender Summe. Unter Einstellungen > Zahltag teilt sich der Zeitstrahl an jedem Zahltag."),
                ("Angekündigte Preisänderungen & Einzelbuchungen", "Mit Preisänderung eintragen gilt ein neuer Tarif ab einem festen Stichtag, während frühere Tage unberührt bleiben. Über das Menü an einer Abbuchung lässt sich genau dieser eine Termin auslassen oder im Betrag anpassen."),
                ("Pausieren, Check-up und Kündigungsersparnis", "Mit Pausieren ruhen Abbuchungen und Hinweise bis zu deinem Rückkehrdatum. Nach der Kündigung beim Anbieter markierst du das Abo als gekündigt; der Tab Jahr zählt die eingesparten Beträge mit.")
            ],
            "faq_title": "Häufige Fragen",
            "faqs": [
                ("Kündigt die App Verträge für mich?", "Nein. Kündigungen erfolgen direkt beim Anbieter. Im Notizfeld lässt sich ein Link als Schaltfläche ablegen, danach markierst du das Abo in der App als gekündigt."),
                ("Greift die App auf Bankkonten oder E-Mails zu?", "Nein. Es gibt keine Konto- oder Bankverbindung und keine automatische Erkennung im Postfach."),
                ("Wie werden mehrere Währungen gezählt?", "Jede Währung behält eigene Summen ohne Internet-Wechselkursumrechnung."),
                ("Wie funktioniert das Widget?", "Das Widget für Home- und Sperrbildschirm zeigt den Betrag bis zum Zahltag sowie die nächsten Abbuchungen und schaltet um Mitternacht weiter."),
                ("Was ist kostenlos und was enthält Pro?", "Bis zu 5 Abos, Zeitstrahl, Zahltag, Preisänderungen, Einzelbuchungen, Widget, Check-up, Sicherungsdatei und Siri-Abfragen sind kostenlos. Abo Manager Pro (Einmalkauf) schaltet unbegrenzte Abos, lokale Erinnerungen, die Jahresauswertung nach Kategorie/Karte und CSV-Export frei."),
                ("Umzug auf ein neues iPhone & Wiederherstellung", "Nutze Einstellungen > Sicherungsdatei speichern sowie Einstellungen > Kauf wiederherstellen für Pro. Erstattungen prüft Apple unter reportaproblem.apple.com.")
            ]
        },
        "privacy": {
            "title": "Datenschutzerklärung",
            "lede": "Deine Abo-Liste bleibt ausschließlich auf deinem iPhone. Kein Konto, kein Tracking, keine Server.",
            "summary_title": "Kurzfassung",
            "rows": [
                ("Erhobene personenbezogene Daten", "Keine"),
                ("Benutzerkonto / Anmeldung", "Nicht vorhanden"),
                ("Bank- oder E-Mail-Zugriff", "Keiner"),
                ("Werbung & Analyse-SDKs", "Keine"),
                ("Speicherort", "Ausschließlich lokal auf dem Gerät & im lokalen Widget-Container"),
                ("Alle Daten löschen", "Einstellungen > Alle Abos löschen oder App entfernen")
            ],
            "sections": [
                ("Lokale Speicherung und Widget", "Alle Einträge liegen in einer Datei innerhalb des privaten App-Speichers auf deinem Gerät; ein lokaler App-Container versorgt die Home- und Sperrbildschirm-Widgets offline."),
                ("Mitteilungen und Siri", "Erinnerungen werden lokal über iOS-Benachrichtigungen geplant; Siri-Kurzbefehle lesen nur aus deiner lokalen Liste."),
                ("In-App-Kauf", "Abo Manager Pro ist ein einmaliger, nicht verbrauchbarer Kauf über Apple StoreKit 2. Zahlungsdaten erhalten wir nicht."),
                ("Backups und CSV-Export", "Exportierte JSON-Sicherungen oder CSV-Dateien verlassen dein iPhone nur über den von dir gewählten Teilen-Dialog."),
                ("Kontakt", "Bei Fragen erreichst du uns per E-Mail unter der oben angegebenen Adresse.")
            ]
        }
    },
    "es-ES": {
        "name": "Español",
        "html_lang": "es",
        "app": "Suscripciones",
        "subtitle": "Control de Renovaciones",
        "nav_help": "Ayuda",
        "nav_privacy": "Política de privacidad",
        "nav_langs": "Todos los idiomas",
        "contact_title": "Soporte y contacto",
        "contact_body": f"Consultas o incidencias sobre Suscripciones: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Actualizado {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "Ayuda y guía",
            "lede": "Lo que sale antes de la nómina: cada cobro en su fecha exacta a lo largo de una línea temporal.",
            "steps_title": "Cómo funciona",
            "steps": [
                ("Registra tus pagos", "Pulsa + e introduce nombre, precio, moneda, frecuencia, primer cobro, categoría, tarjeta y personas que comparten el gasto. Activa prueba gratuita si corresponde."),
                ("Sigue la línea y tu día de nómina", "La pestaña Línea muestra los próximos cobros con total acumulado. Define tu día de pago en Ajustes > Día de nómina para dividir el cálculo por nóminas."),
                ("Cambios de precio anunciados y cobros puntuales", "Usa Va a cambiar de precio para programar una subida desde su día de entrada en vigor sin alterar el pasado. En un cobro concreto puedes omitirlo o ajustar solo esa fecha."),
                ("Pausar, revisar y cancelar", "Pon en pausa cualquier servicio temporalmente o márcalo como cancelado tras darlo de baja con el proveedor para sumar el ahorro en la pestaña Año.")
            ],
            "faq_title": "Preguntas frecuentes",
            "faqs": [
                ("¿La app cancela suscripciones automáticamente?", "No. Cancela directamente con el proveedor y después selecciona Marcar como cancelada dentro de la app."),
                ("¿Se conecta al banco o lee correos?", "No. No requiere cuenta, no se conecta a entidades bancarias ni analiza tu correo."),
                ("¿Cómo trata distintas divisas?", "Cada moneda mantiene su propio total separado sin realizar conversiones automáticas por internet."),
                ("¿Qué ofrece la versión gratuita y qué incluye Pro?", "Hasta 5 suscripciones, línea, día de nómina, cambios de precio, ajustes puntuales, widget, revisión y copias de seguridad son gratuitos. Suscripciones Pro (pago único) desbloquea registros ilimitados, avisos locales, gráficos anuales por categoría/tarjeta y CSV."),
                ("Copia de seguridad, restauración y reembolsos", "Guarda o restaura tu archivo en Ajustes. Si cambiaste de iPhone usa Restaurar compra; los reembolsos los gestiona Apple en reportaproblem.apple.com.")
            ]
        },
        "privacy": {
            "title": "Política de privacidad",
            "lede": "Tu lista vive únicamente en tu iPhone. Sin cuentas, sin análisis de uso y sin servidores externos.",
            "summary_title": "Resumen",
            "rows": [
                ("Datos personales recopilados", "Ninguno"),
                ("Registro de cuenta", "No requerido"),
                ("Conexión bancaria", "Ninguna"),
                ("Publicidad y rastreadores", "Ninguno"),
                ("Almacenamiento", "Local en el dispositivo y contenedor compartido del widget"),
                ("Borrado completo", "Ajustes > Eliminar todas las suscripciones")
            ],
            "sections": [
                ("Almacenamiento local y widgets", "Tu lista se guarda localmente en el dispositivo junto con una copia local para mostrar los widgets de pantalla de inicio y bloqueo sin conexión."),
                ("Recordatorios y Siri", "Las notificaciones y respuestas de Siri funcionan íntegramente de manera local."),
                ("Compra integrada", "Suscripciones Pro se procesa exclusivamente mediante Apple StoreKit 2 como compra única."),
                ("Copias y CSV", "Tus copias JSON o archivos CSV solo salen del iPhone si decides compartirlos."),
                ("Contacto", "Puedes escribirnos cuando lo necesites a la dirección indicada abajo.")
            ]
        }
    },
    "fr-FR": {
        "name": "Français",
        "html_lang": "fr",
        "app": "Abonnements",
        "subtitle": "Suivi et Rappels",
        "nav_help": "Aide",
        "nav_privacy": "Confidentialité",
        "nav_langs": "Toutes les langues",
        "contact_title": "Assistance et contact",
        "contact_body": f"Questions ou retours sur Abonnements : <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Mise à jour {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "Aide et guide",
            "lede": "Ce qui part avant la paie : chaque prélèvement placé au jour exact sur une ligne claire.",
            "steps_title": "Fonctionnement",
            "steps": [
                ("Ajouter vos abonnements", "Touchez + et saisissez le nom, le montant, la devise, la fréquence, la première date, la catégorie, la carte et le partage éventuel. Activez l’option d’essai gratuit si besoin."),
                ("Suivre la ligne et la date de paie", "L’onglet Ligne présente les prochains prélèvements jour par jour avec le cumul. Réglez votre jour de paie dans Réglages pour scinder la ligne à chaque salaire."),
                ("Hausses annoncées et montants exceptionnels", "Planifiez un changement de prix à partir d’une date donnée sans modifier l’historique, ou ignorez / modifiez un seul prélèvement ponctuel."),
                ("Mettre en pause, faire le bilan et résilier", "Suspendez temporairement un service avec Mettre en pause ou marquez-le comme résilié après annulation auprès du fournisseur afin de suivre vos économies sur l’onglet Année.")
            ],
            "faq_title": "Questions fréquentes",
            "faqs": [
                ("L’app résilie-t-elle mes contrats automatiquement ?", "Non. Résiliez auprès du fournisseur puis marquez l’abonnement comme résilié dans l’application."),
                ("Y a-t-il une connexion bancaire ou e-mail ?", "Non. Aucune donnée bancaire ni boîte mail n’est consultée ; tout repose sur votre saisie."),
                ("Comment sont gérées plusieurs devises ?", "Chaque devise garde son propre total sans conversion automatique en ligne."),
                ("Différence entre version gratuite et Pro ?", "Jusqu’à 5 abonnements, ligne, paie, hausses annoncées, bilan, widgets, sauvegarde JSON et Siri sont gratuits. Abonnements Pro (achat unique) débloque le nombre illimité, les rappels locaux, l’année détaillée et l’export CSV."),
                ("Sauvegarde, restauration et remboursements", "Exportez ou importez votre fichier dans Réglages. Restaurez Pro depuis Réglages > Restaurer l’achat. Les remboursements relèvent d’Apple sur reportaproblem.apple.com.")
            ]
        },
        "privacy": {
            "title": "Politique de confidentialité",
            "lede": "Vos données restent strictement sur votre iPhone. Aucun compte, aucune publicité, aucun serveur.",
            "summary_title": "En bref",
            "rows": [
                ("Données collectées par nous", "Aucune"),
                ("Création de compte", "Non requise"),
                ("Accès bancaire", "Aucun"),
                ("Statistiques et pub", "Aucune"),
                ("Stockage", "Fichier local sur l’appareil et conteneur widget local"),
                ("Suppression", "Réglages > Supprimer tous les abonnements")
            ],
            "sections": [
                ("Stockage local et widgets", "Votre liste est enregistrée localement sur votre appareil et partagée localement avec les widgets sans accès réseau."),
                ("Rappels et Siri", "Les notifications et raccourcis Siri s’exécutent uniquement sur l’appareil."),
                ("Achat intégré", "Abonnements Pro est un achat unique géré exclusivement par Apple StoreKit 2."),
                ("Sauvegardes et CSV", "Les fichiers générés ne quittent l’appareil que lorsque vous les enregistrez ou partagez."),
                ("Contact", "Pour toute question, contactez-nous par e-mail à l’adresse indiquée.")
            ]
        }
    },
    "it": {
        "name": "Italiano",
        "html_lang": "it",
        "app": "Abbonamenti",
        "subtitle": "Spese e Scadenze",
        "nav_help": "Aiuto",
        "nav_privacy": "Privacy",
        "nav_langs": "Tutte le lingue",
        "contact_title": "Supporto e contatti",
        "contact_body": f"Domande o segnalazioni su Abbonamenti: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Aggiornato {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "Aiuto e guida",
            "lede": "Cosa esce prima dello stipendio: ogni addebito nel suo giorno su una linea ordinata.",
            "steps_title": "Come funziona",
            "steps": [
                ("Inserisci gli abbonamenti", "Tocca + e inserisci nome, prezzo, valuta, cadenza, prima data, categoria, carta e quota condivisa, oppure la data di fine prova."),
                ("Linea e giorno di paga", "La scheda Linea elenca i prossimi addebiti in ordine di giorno con il totale progressivo. Imposta la data dello stipendio in Impostazioni."),
                ("Variazioni future e singoli addebiti", "Registra un nuovo prezzo dalla sua data di decorrenza o modifica/salta un singolo addebito senza toccare il prezzo base."),
                ("Pausa, revisione e risparmio", "Metti in pausa un servizio temporaneo oppure segnalo come disdetto dopo aver annullato presso il fornitore per vedere il risparmio annuale.")
            ],
            "faq_title": "Domande frequenti",
            "faqs": [
                ("L’app disdice automaticamente gli abbonamenti?", "No. La disdetta va effettuata presso il servizio; poi puoi segnarlo come disdetto nell’app."),
                ("Si collega a banche o e-mail?", "No, l’app è completamente manuale e offline."),
                ("Come funzionano valute diverse?", "Ogni valuta mantiene il proprio totale separato senza tassi di cambio online."),
                ("Cosa include la versione gratuita e cosa Pro?", "Fino a 5 abbonamenti, linea, giorno di paga, variazioni future, widget, revisione, backup e Siri sono inclusi. Abbonamenti Pro è un acquisto unico per voci illimitate, promemoria, grafici annuali ed esportazione CSV."),
                ("Backup, ripristino e rimborsi", "Esporta/importa il backup dalle Impostazioni. Usa Ripristina acquisto per Pro; i rimborsi sono gestiti da Apple su reportaproblem.apple.com.")
            ]
        },
        "privacy": {
            "title": "Informativa sulla privacy",
            "lede": "La tua lista resta solo sul tuo iPhone. Nessun account, nessuna telemetria, nessun server.",
            "summary_title": "Riepilogo",
            "rows": [
                ("Dati raccolti", "Nessuno"),
                ("Account", "Non richiesto"),
                ("Accesso bancario", "Nessuno"),
                ("Pubblicità o SDK esterni", "Nessuno"),
                ("Archiviazione", "Solo locale sul dispositivo e container locale per il widget"),
                ("Cancellazione", "Impostazioni > Elimina tutti gli abbonamenti")
            ],
            "sections": [
                ("Archiviazione locale", "I dati sono salvati in locale sull’iPhone e condivisi localmente con i widget senza traffico di rete."),
                ("Notifiche e Siri", "Promemoria e comandi Siri elaborano i dati esclusivamente sul dispositivo."),
                ("Acquisti in-app", "Abbonamenti Pro è gestito da Apple tramite StoreKit 2 senza esporre dati di pagamento."),
                ("Backup e CSV", "I file esportati escono dal dispositivo solo su tua azione esplicita."),
                ("Contatti", "Scrivici all’indirizzo e-mail indicato per qualsiasi chiarimento.")
            ]
        }
    },
    "nl-NL": {
        "name": "Nederlands",
        "html_lang": "nl",
        "app": "Abonnementen",
        "subtitle": "Overzicht en Meldingen",
        "nav_help": "Hulp",
        "nav_privacy": "Privacybeleid",
        "nav_langs": "Alle talen",
        "contact_title": "Contact & ondersteuning",
        "contact_body": f"Vragen over Abonnementen: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Bijgewerkt {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "Hulp & uitleg",
            "lede": "Wat er vóór je betaaldag afgaat: elke afschrijving op de eigen datum langs één tijdlijn.",
            "steps_title": "Zo werkt het",
            "steps": [
                ("Voeg abonnementen toe", "Tik op + en noteer naam, prijs, valuta, ritme, begindatum, categorie, betaalkaart en gedeelde kosten of proefperiode."),
                ("Lijn en betaaldag", "Het tabblad Lijn ordent komende afschrijvingen per dag. Stel je betaaldag in via Instellingen om de splitsing tot je volgende salaris te zien."),
                ("Prijswijzigingen en losse betalingen", "Plan een aangekondigde prijswijziging vanaf de ingangsdatum of sla één afschrijving over zonder de vaste prijs te wijzigen."),
                ("Pauzeren, check-up en opzeggen", "Zet een abonnement tijdelijk op pauze of markeer het na opzegging bij de aanbieder als opgezegd om besparingen bij te houden.")
            ],
            "faq_title": "Veelgestelde vragen",
            "faqs": [
                ("Zegt de app abonnementen automatisch op?", "Nee. Je zegt zelf op bij de aanbieder en markeert dat daarna in de app."),
                ("Maakt de app verbinding met bank of e-mail?", "Nee, alles wat in de app staat vul je zelf lokaal in."),
                ("Meerdere valuta’s?", "Elke valuta heeft een eigen totaal zonder automatische wisselkoersen."),
                ("Gratis vs. Pro?", "Tot 5 abonnementen, de lijn, betaaldag, prijswijzigingen, widgets, check-up, back-up en Siri zijn gratis. Abonnementen Pro (eenmalige aankoop) biedt onbeperkt aantal abonnementen, meldingen, jaaroverzicht en CSV-export."),
                ("Overzetten en terugbetaling", "Maak een back-upbestand via Instellingen of herstel Pro via Aankoop herstellen. Terugbetalingen lopen via reportaproblem.apple.com.")
            ]
        },
        "privacy": {
            "title": "Privacybeleid",
            "lede": "Je gegevens staan alleen op jouw iPhone. Geen account, geen tracking, geen servers.",
            "summary_title": "Overzicht",
            "rows": [
                ("Verzamelde gegevens", "Geen"),
                ("Account vereist", "Nee"),
                ("Bankkoppeling", "Geen"),
                ("Advertenties of trackers", "Geen"),
                ("Opslag", "Alleen lokaal op het apparaat en lokale widget-opslag"),
                ("Verwijderen", "Instellingen > Verwijder alle abonnementen")
            ],
            "sections": [
                ("Lokale opslag en widgets", "Gegevens blijven binnen de lokale opslag op jouw iPhone en voorzien widgets lokaal van info."),
                ("Herinneringen en Siri", "Meldingen en Siri-antwoorden werken volledig op het apparaat zelf."),
                ("In-app aankoop", "Abonnementen Pro verloopt als eenmalige aankoop via Apple StoreKit 2."),
                ("Back-up en CSV", "Bestanden verlaten het apparaat alleen wanneer je ze zelf deelt of bewaart."),
                ("Contact", "Voor vragen kun je mailen naar het bovenstaande adres.")
            ]
        }
    },
    "pt-BR": {
        "name": "Português (Brasil)",
        "html_lang": "pt-BR",
        "app": "Assinaturas",
        "subtitle": "Controle de Cobranças",
        "nav_help": "Ajuda",
        "nav_privacy": "Privacidade",
        "nav_langs": "Todos os idiomas",
        "contact_title": "Suporte e contato",
        "contact_body": f"Dúvidas sobre Assinaturas: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Atualizado {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "Ajuda e guia",
            "lede": "O que sai antes do salário: cada cobrança no seu dia exato ao longo de uma única linha.",
            "steps_title": "Como usar",
            "steps": [
                ("Cadastre seus serviços", "Toque em + e informe nome, valor, moeda, frequência, primeira cobrança, categoria, cartão e divisão entre pessoas."),
                ("Linha do tempo e salário", "A aba Linha mostra as próximas cobranças em ordem cronológica. Defina o dia do seu salário em Ajustes para ver quanto sai antes do próximo pagamento."),
                ("Reajustes e cobranças avulsas", "Registre um aumento futuro a partir da data anunciada ou pule/edite o valor de apenas uma cobrança pontual."),
                ("Pausar, revisar e cancelar", "Pause uma assinatura quando não estiver usando ou marque como cancelada após encerrar com o fornecedor para somar a economia na aba Ano.")
            ],
            "faq_title": "Perguntas frequentes",
            "faqs": [
                ("O aplicativo cancela os serviços sozinho?", "Não. O cancelamento é feito diretamente com o serviço; no app você marca como cancelada."),
                ("Conecta ao banco ou lê e-mails?", "Não. Tudo é inserido manualmente e permanece local."),
                ("Como funcionam moedas diferentes?", "Cada moeda mantém seu total separado, sem conversão pela internet."),
                ("O que é gratuito e o que muda no Pro?", "Até 5 assinaturas, linha, salário, reajustes, widgets, revisão, backup e Siri são gratuitos. Assinaturas Pro é pagamento único para assinaturas ilimitadas, lembretes, gráficos anuais e CSV."),
                ("Backup, restauração e reembolso", "Salve e restaure o arquivo de backup em Ajustes. Use Restaurar compra para reativar o Pro; reembolsos passam pela Apple em reportaproblem.apple.com.")
            ]
        },
        "privacy": {
            "title": "Política de Privacidade",
            "lede": "Sua lista fica apenas no seu iPhone. Sem conta, sem rastreadores e sem servidores.",
            "summary_title": "Resumo",
            "rows": [
                ("Dados coletados", "Nenhum"),
                ("Login obrigatório", "Não"),
                ("Acesso bancário", "Nenhum"),
                ("Anúncios ou SDKs de terceiros", "Nenhum"),
                ("Armazenamento", "Apenas local no dispositivo e contêiner do widget"),
                ("Exclusão", "Ajustes > Apagar todas as assinaturas")
            ],
            "sections": [
                ("Armazenamento local", "Seus dados ficam gravados localmente no aparelho e no contêiner local do widget."),
                ("Lembretes e Siri", "Notificações e atalhos da Siri funcionam inteiramente no aparelho."),
                ("Compra no app", "Assinaturas Pro é uma compra única processada exclusivamente pela Apple via StoreKit 2."),
                ("Backup e CSV", "Arquivos exportados só saem do iPhone quando você escolhe salvá-los ou compartilhá-los."),
                ("Contato", "Escreva para o e-mail de suporte sempre que precisar.")
            ]
        }
    },
    "ru": {
        "name": "Русский",
        "html_lang": "ru",
        "app": "Подписки",
        "subtitle": "Трекер Списаний",
        "nav_help": "Справка",
        "nav_privacy": "Конфиденциальность",
        "nav_langs": "Все языки",
        "contact_title": "Поддержка и контакты",
        "contact_body": f"Вопросы по приложению Подписки: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Обновлено {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "Справка и руководство",
            "lede": "Сколько уйдёт до зарплаты: наглядная лента предстоящих списаний по дням.",
            "steps_title": "Как это работает",
            "steps": [
                ("Добавьте подписки", "Нажмите + и укажите название, цену, валюту, периодичность, первую дату, категорию, карту и число участников. При необходимости включите пробный период."),
                ("Лента и дата зарплаты", "Вкладка Лента располагает списания по датам. Укажите день зарплаты в Настройках, чтобы видеть сумму до следующей выплаты."),
                ("Будущие изменения цен и разовые списания", "Добавьте объявленное повышение цены с даты начала действия или пропустите/измените одно конкретное списание."),
                ("Пауза, проверка и отмена", "Ставьте сервис на паузу без удаления или отмечайте отмену после отказа у провайдера, чтобы копить экономию во вкладке Год.")
            ],
            "faq_title": "Частые вопросы",
            "faqs": [
                ("Отменяет ли приложение подписки само?", "Нет. Сначала отмените подписку у сервиса, затем отметьте это в приложении."),
                ("Подключается ли к банкам или почте?", "Нет. Все данные вводятся вручную и хранятся на устройстве."),
                ("Как учитываются разные валюты?", "Для каждой валюты считается отдельный итог без конвертации курсов через сеть."),
                ("Что бесплатно, а что в Pro?", "До 5 подписок, лента, день зарплаты, изменения цен, виджеты, проверка, резервная копия и Siri бесплатны. Подписки Pro (разовая покупка) снимает лимит и открывает уведомления, годовую аналитику и CSV."),
                ("Перенос и возврат средств", "Сохраните и восстановите резервную копию в Настройках. Покупку Pro можно вернуть кнопкой Восстановить покупку; возвраты оформляются через reportaproblem.apple.com.")
            ]
        },
        "privacy": {
            "title": "Политика конфиденциальности",
            "lede": "Ваш список хранится только на вашем iPhone. Без аккаунтов, аналитики и серверов.",
            "summary_title": "Кратко",
            "rows": [
                ("Собираемые данные", "Нет"),
                ("Регистрация", "Не требуется"),
                ("Доступ к банкам или почте", "Отсутствует"),
                ("Реклама и трекеры", "Отсутствуют"),
                ("Хранение", "Локально на устройстве и в локальном контейнере виджета"),
                ("Удаление данных", "Настройки > Удалить все подписки")
            ],
            "sections": [
                ("Локальное хранение", "Данные хранятся в одном файле на вашем iPhone и локально доступны виджетам без отправки в сеть."),
                ("Уведомления и Siri", "Напоминания планируются и команды Siri выполняются локально на устройстве."),
                ("Встроенные покупки", "Подписки Pro оформляется как разовая покупка через Apple StoreKit 2."),
                ("Резервные копии и CSV", "Экспортированные файлы покидают устройство только по вашему выбору."),
                ("Контакты", "По всем вопросам пишите на указанный адрес электронной почты.")
            ]
        }
    },
    "ja": {
        "name": "日本語",
        "html_lang": "ja",
        "app": "サブスク管理",
        "subtitle": "更新日リマインダー",
        "nav_help": "ヘルプ",
        "nav_privacy": "プライバシー",
        "nav_langs": "すべての言語",
        "contact_title": "サポート・お問い合わせ",
        "contact_body": f"サブスク管理に関するご質問: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>",
        "updated": f"更新日 {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "ヘルプと使い方",
            "lede": "次の給料日までに出ていく金額を、日ごとの1本のラインで確認できます。",
            "steps_title": "使い方",
            "steps": [
                ("サブスクを登録", "＋から名前・料金・通貨・周期・初回支払日・カテゴリ・カード・割り勘人数を入力します。無料トライアルの終了日も記録できます。"),
                ("ラインと給料日", "「ライン」タブで次の支払いを日付順に並べます。設定から給料日を登録すると、次の給料日までの支出額が区切られます。"),
                ("値上げ予定と1回限りの変更", "告知された価格改定を開始日つきで記録したり、特定の1回だけスキップ・金額変更したりできます。"),
                ("一時保留・見直し・解約記録", "使わない期間は「保留にする」で止め、サービス側で解約したら「解約済みにする」を選ぶと年間タブに節約額が貯まります。")
            ],
            "faq_title": "よくある質問",
            "faqs": [
                ("アプリが自動で解約してくれますか？", "いいえ。提供元のサイトやAppleのサブスクリプション画面で解約してから、アプリ上で「解約済みにする」を押してください。"),
                ("銀行口座やメールと連携しますか？", "いいえ。口座接続やメール読み取りは行わず、入力した情報だけをローカルに保存します。"),
                ("複数通貨の扱いは？", "通貨ごとに合計を分けて表示します。ネット経由の自動換算は行いません。"),
                ("無料版とProの違いは？", "5件まで登録、ライン、給料日区切り、価格変更、ウィジェット、見直し、バックアップ、Siriは無料です。サブスク管理 Pro（買い切り）で件数無制限、リマインダー通知、月別・カード別グラフ、CSV出力が利用できます。"),
                ("機種変更と返金について", "設定からバックアップ保存・復元ができます。Proの再適用は「購入を復元」、返金はAppleの reportaproblem.apple.com から手続きできます。")
            ]
        },
        "privacy": {
            "title": "プライバシーポリシー",
            "lede": "データはあなたのiPhoneの中だけに保存されます。アカウントも追跡もサーバーもありません。",
            "summary_title": "概要",
            "rows": [
                ("収集する個人情報", "なし"),
                ("アカウント登録", "不要"),
                ("銀行・メール連携", "なし"),
                ("広告・解析SDK", "なし"),
                ("保存先", "端末内ストレージおよびウィジェット用ローカル領域のみ"),
                ("データの削除", "設定 > すべてのサブスクを削除")
            ],
            "sections": [
                ("端末内保存とウィジェット", "登録データはiPhone内のアプリ領域に保存され、ホーム画面・ロック画面ウィジェットもオフラインで参照します。"),
                ("通知とSiri", "通知の予約やSiriからの参照はすべて端末内で完結します。"),
                ("アプリ内課金", "サブスク管理 ProはAppleのStoreKit 2を通じた1回限りの買い切り購入です。"),
                ("バックアップとCSV", "書き出したファイルはユーザーが共有先を選んだ場合のみ端末外へ渡されます。"),
                ("お問い合わせ", "ご不明点があれば記載のメールアドレスまでご連絡ください。")
            ]
        }
    },
    "ko": {
        "name": "한국어",
        "html_lang": "ko",
        "app": "구독 관리",
        "subtitle": "결제일 및 지출 추적",
        "nav_help": "도움말",
        "nav_privacy": "개인정보 처리방침",
        "nav_langs": "모든 언어",
        "contact_title": "지원 및 문의",
        "contact_body": f"구독 관리 문의 및 의견: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>",
        "updated": f"업데이트 {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "도움말 및 가이드",
            "lede": "월급날 전에 나가는 돈 한눈에: 입력한 날짜와 금액에 맞춰 정렬되는 결제 타임라인.",
            "steps_title": "사용 방법",
            "steps": [
                ("구독 항목 입력", "+ 버튼을 눌러 이름, 금액, 통화, 주기, 첫 결제일, 카테고리, 카드, 분담 인원을 입력합니다. 무료 체험 종료일도 설정할 수 있습니다."),
                ("타임라인과 월급날 기준", "타임라인 탭은 다가오는 결제를 날짜순으로 보여줍니다. 설정에서 월급날을 지정하면 다음 월급날 전까지 빠져나가는 금액이 구분됩니다."),
                ("가격 인상 예고 및 단발성 결제 수정", "예정된 가격 변동을 시작일과 함께 기록하거나 이번 한 번만 결제를 건너뛰고 금액을 바꿀 수 있습니다."),
                ("일시정지, 점검 및 해지 절약액", "잠시 쉬는 서비스는 일시정지로 두고, 실제 제공업체에서 해지한 뒤 해지됨으로 표시하면 연간 탭에서 절약된 금액을 확인할 수 있습니다.")
            ],
            "faq_title": "자주 묻는 질문",
            "faqs": [
                ("앱에서 바로 구독이 해지되나요?", "아니요. 서비스 웹사이트나 Apple 구독 관리에서 직접 해지한 뒤 앱에 해지됨으로 기록합니다."),
                ("은행 계좌나 이메일과 연동되나요?", "아니요. 계좌 연동이나 이메일 수집 없이 사용자가 직접 입력한 내용만 기기에 저장됩니다."),
                ("여러 통화는 어떻게 계산되나요?", "통화별 합계를 따로 표시하며 온라인 환율 변환은 하지 않습니다."),
                ("무료 버전과 Pro의 차이는?", "최대 5개 구독, 타임라인, 월급날 기준, 가격 변동, 위젯, 점검, 백업 파일 및 Siri 응답이 무료입니다. 구독 관리 Pro는 1회 결제로 무제한 등록, 로컬 알림, 월별/카드별 차트, CSV 내보내기를 제공합니다."),
                ("기기 변경 및 환불", "설정에서 백업 파일을 저장하거나 복원할 수 있습니다. Pro 복원은 구입 복원 버튼을, 환불은 reportaproblem.apple.com에서 진행합니다.")
            ]
        },
        "privacy": {
            "title": "개인정보 처리방침",
            "lede": "구독 목록은 iPhone 내부에만 저장됩니다. 계정도, 추적도, 서버도 없습니다.",
            "summary_title": "요약",
            "rows": [
                ("수집하는 개인정보", "없음"),
                ("로그인 및 계정", "불필요"),
                ("금융/이메일 연동", "없음"),
                ("광고 및 분석 도구", "없음"),
                ("저장 위치", "기기 내부 저장소 및 위젯 로컬 컨테이너"),
                ("전체 삭제", "설정 > 모든 구독 삭제")
            ],
            "sections": [
                ("기기 내 저장", "목록은 iPhone 내 앱 전용 파일에 보관되며 위젯 역시 네트워크 없이 로컬 영역만 읽습니다."),
                ("알림 및 Siri", "모든 알림 예약과 Siri 답변은 기기 내부에서만 처리됩니다."),
                ("앱 내 구입", "구독 관리 Pro는 Apple StoreKit 2를 통해 처리되는 일회성 구입 항목입니다."),
                ("백업 및 CSV", "내보낸 파일은 사용자가 공유를 선택한 경우에만 외부로 전달됩니다."),
                ("문의", "문의 사항은 상단 이메일로 보내 주세요.")
            ]
        }
    },
    "zh-Hans": {
        "name": "简体中文",
        "html_lang": "zh-Hans",
        "app": "订阅管理",
        "subtitle": "续费与发薪日提醒",
        "nav_help": "帮助",
        "nav_privacy": "隐私政策",
        "nav_langs": "所有语言",
        "contact_title": "支持与联系",
        "contact_body": f"如有问题或建议，请联系：<a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>",
        "updated": f"更新日期 {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş",
        "help": {
            "title": "使用帮助与指南",
            "lede": "发薪日前会扣走多少钱：按日期顺序列出每笔即将到来的续费。",
            "steps_title": "使用步骤",
            "steps": [
                ("添加订阅项目", "轻点 +，填写名称、金额、币种、周期、首次扣费日期、分类、银行卡以及分摊人数；如有免费试用可开启并设置结束日。"),
                ("查看时间线与发薪日区间", "时间线标签按日期排列所有扣费并显示累计总额。在设置中设置发薪日后，时间线会按发薪周期分段统计。"),
                ("未来调价与单次扣费调整", "记录即将生效的新价格及起始日，不影响之前记录；也可以针对某一次扣费选择跳过或填写单次金额。"),
                ("暂停、体检与取消节省", "暂停期间不计入总额也不发提醒；在服务商处取消订阅后再标记为已取消，即可在年度标签统计节省金额。")
            ],
            "faq_title": "常见问题",
            "faqs": [
                ("应用会自动帮我退订吗？", "不会。请先前往服务商或 Apple 订阅设置取消，再在应用中标记为已取消。"),
                ("会读取银行账单或电子邮件吗？", "不会。本应用不连接银行也不读取邮件，仅记录你手动输入的内容。"),
                ("支持多种货币吗？", "支持。不同货币会分别汇总统计，不会联网自动换算汇率。"),
                ("免费版与 Pro 有何区别？", "免费支持最多 5 项订阅、时间线、发薪日统计、调价预告、桌面/锁屏小组件、体检、备份文件和 Siri 问答。订阅管理 Pro 为一次性买断，解锁无限订阅、本地通知提醒、年度图表与 CSV 导出。"),
                ("备份恢复与退款", "可在设置中保存备份或从备份恢复，换机后点击恢复购买即可恢复 Pro；退款请通过 Apple 的 reportaproblem.apple.com 申请。")
            ]
        },
        "privacy": {
            "title": "隐私政策",
            "lede": "你的订阅清单仅保存在本地 iPhone 上。无需账号、无追踪、无远程服务器。",
            "summary_title": "概要",
            "rows": [
                ("收集的个人数据", "无"),
                ("账号登录", "不需要"),
                ("银行或邮箱访问", "无"),
                ("广告与分析 SDK", "无"),
                ("数据存储", "仅限设备本地私有存储及小组件共享容器"),
                ("清除全部数据", "设置 > 删除所有订阅")
            ],
            "sections": [
                ("本地存储与小组件", "清单数据保存在你设备本地，主屏幕与锁屏小组件仅通过本机共享容器离线读取。"),
                ("通知与 Siri", "续费提醒和 Siri 捷径均完全在设备本地执行。"),
                ("App 内购买", "订阅管理 Pro 通过 Apple StoreKit 2 一次性买断，我们无法接触你的支付信息。"),
                ("备份与导出", "导出的 JSON 备份或 CSV 表格仅在你主动共享或保存时离开应用。"),
                ("联系方式", "如有任何隐私相关问题，请发送邮件至上方支持邮箱。")
            ]
        }
    }
}


def lang_bar(current: str, page: str, in_root: bool) -> str:
    chips = []
    for loc, d in LOCALES.items():
        href = f"{loc}/{page}" if in_root else f"../{loc}/{page}"
        cls = "lang-chip current" if loc == current else "lang-chip"
        chips.append(f'<a class="{cls}" href="{href}">{html.escape(d["name"])}</a>')
    return f'<div class="lang-strip">{"".join(chips)}</div>'


def render_help(locale: str, data: dict, in_root: bool = False) -> str:
    h = data["help"]
    icon_src = "assets/icon.png" if in_root else "../assets/icon.png"
    canonical = f"{BASE_URL}/help.html" if in_root else f"{BASE_URL}/{locale}/help.html"
    idx_href = "index.html" if in_root else "../index.html"
    steps_html = "".join(
        f"<li><strong>{html.escape(t)}</strong>{html.escape(b)}</li>"
        for t, b in h["steps"]
    )
    faq_html = "".join(
        f'<div class="faq-card"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></div>'
        for q, a in h["faqs"]
    )
    return f"""<!doctype html>
<html lang="{data['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(data['app'])} — {html.escape(h['title'])}</title>
<link rel="canonical" href="{canonical}">
<style>{CSS}</style>
</head>
<body>
<div class="route-header" aria-hidden="true"></div>
<main>
  <div class="hero">
    <img src="{icon_src}" alt="{html.escape(data['app'])}">
    <div>
      <div class="eyebrow">{html.escape(data['app'])} · {html.escape(data['subtitle'])}</div>
      <h1>{html.escape(h['title'])}</h1>
    </div>
  </div>
  <p class="lede">{html.escape(h['lede'])}</p>
  <nav class="primary-nav">
    <a href="help.html">{html.escape(data['nav_help'])}</a>
    <a href="privacy.html">{html.escape(data['nav_privacy'])}</a>
    <a href="{idx_href}">{html.escape(data['nav_langs'])}</a>
  </nav>
  {lang_bar(locale, "help.html", in_root)}
  <h2>{html.escape(h['steps_title'])}</h2>
  <ol class="stops">{steps_html}</ol>
  <h2>{html.escape(h['faq_title'])}</h2>
  {faq_html}
  <h2>{html.escape(data['contact_title'])}</h2>
  <p>{data['contact_body']}</p>
  <footer>{html.escape(data['updated'])}</footer>
</main>
</body>
</html>
"""


def render_privacy(locale: str, data: dict, in_root: bool = False) -> str:
    p = data["privacy"]
    icon_src = "assets/icon.png" if in_root else "../assets/icon.png"
    canonical = f"{BASE_URL}/privacy.html" if in_root else f"{BASE_URL}/{locale}/privacy.html"
    idx_href = "index.html" if in_root else "../index.html"
    rows_html = "".join(
        f"<tr><td><strong>{html.escape(k)}</strong></td><td>{html.escape(v)}</td></tr>"
        for k, v in p["rows"]
    )
    sec_html = "".join(
        f'<div class="privacy-block"><h2>{html.escape(t)}</h2><p>{html.escape(b)}</p></div>'
        for t, b in p["sections"]
    )
    return f"""<!doctype html>
<html lang="{data['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(data['app'])} — {html.escape(p['title'])}</title>
<link rel="canonical" href="{canonical}">
<style>{CSS}</style>
</head>
<body>
<div class="route-header" aria-hidden="true"></div>
<main>
  <div class="hero">
    <img src="{icon_src}" alt="{html.escape(data['app'])}">
    <div>
      <div class="eyebrow">{html.escape(data['app'])} · {html.escape(data['subtitle'])}</div>
      <h1>{html.escape(p['title'])}</h1>
    </div>
  </div>
  <p class="lede">{html.escape(p['lede'])}</p>
  <nav class="primary-nav">
    <a href="help.html">{html.escape(data['nav_help'])}</a>
    <a href="privacy.html">{html.escape(data['nav_privacy'])}</a>
    <a href="{idx_href}">{html.escape(data['nav_langs'])}</a>
  </nav>
  {lang_bar(locale, "privacy.html", in_root)}
  <h2>{html.escape(p['summary_title'])}</h2>
  <table class="fact-table"><tbody>{rows_html}</tbody></table>
  {sec_html}
  <h2>{html.escape(data['contact_title'])}</h2>
  <p>{data['contact_body']}</p>
  <footer>{html.escape(data['updated'])}</footer>
</main>
</body>
</html>
"""


def render_index() -> str:
    items = "".join(
        f'<li><strong>{html.escape(d["name"])}</strong><br>'
        f'<a href="{loc}/help.html">{html.escape(d["nav_help"])}</a> · '
        f'<a href="{loc}/privacy.html">{html.escape(d["nav_privacy"])}</a></li>'
        for loc, d in LOCALES.items()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Subscriptions: Renewal Tracker — Help &amp; Privacy</title>
<link rel="canonical" href="{BASE_URL}/">
<style>{CSS}</style>
</head>
<body>
<div class="route-header" aria-hidden="true"></div>
<main>
  <div class="hero">
    <img src="assets/icon.png" alt="Subscriptions">
    <div>
      <div class="eyebrow">Subscriptions · Renewal Tracker</div>
      <h1>Help &amp; Privacy</h1>
    </div>
  </div>
  <p class="lede">What leaves before payday: a chronological charge line and local renewal tracker for iOS. Choose your language below.</p>
  <nav class="primary-nav">
    <a href="help.html">English Help</a>
    <a href="privacy.html">Privacy Policy</a>
  </nav>
  <ul class="locale-grid">{items}</ul>
  <footer>Updated {UPDATED} · Subscriptions (app.klarwerk.subscriptions) · Hayri Odabaş · <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></footer>
</main>
</body>
</html>
"""


def main() -> None:
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    for locale, data in LOCALES.items():
        loc_dir = ROOT / locale
        loc_dir.mkdir(parents=True, exist_ok=True)
        (loc_dir / "help.html").write_text(render_help(locale, data, in_root=False), encoding="utf-8")
        (loc_dir / "privacy.html").write_text(render_privacy(locale, data, in_root=False), encoding="utf-8")
    (ROOT / "index.html").write_text(render_index(), encoding="utf-8")
    (ROOT / "help.html").write_text(render_help("en-US", LOCALES["en-US"], in_root=True), encoding="utf-8")
    (ROOT / "privacy.html").write_text(render_privacy("en-US", LOCALES["en-US"], in_root=True), encoding="utf-8")
    print(f"Generated {len(LOCALES) * 2 + 3} HTML pages in {ROOT}")


if __name__ == "__main__":
    main()
