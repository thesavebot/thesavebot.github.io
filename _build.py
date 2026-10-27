"""Собирает privacy.html, terms.html, robots.txt, sitemap.xml (общая шапка и подвал). python _build.py"""
from pathlib import Path

D = Path(__file__).parent
SITE = "https://thesavebot.github.io/"
BOT = '<a href="https://t.me/THE_SaveChatBot">@THE_SaveChatBot</a>'
HR = '<hr id="en" style="margin:48px 0;border:0;border-top:1px solid var(--line)">'


def page(name, title, body):
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — THE.SaveBot</title>
<link rel="canonical" href="{SITE}{name}">
<link rel="icon" href="favicon.png" type="image/png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><div class="wrap"><img src="icon.png" alt=""><b><a href="./" style="color:inherit;text-decoration:none">THE.SaveBot</a></b><nav><a href="#en">English</a></nav></div></header>
<main class="wrap doc">
{body}
</main>
<footer><div class="wrap"><span>© 2026 THE.SaveBot</span><span class="sp"></span><a href="./">Главная</a><a href="privacy.html">Политика конфиденциальности</a><a href="terms.html">Условия использования</a></div></footer>
</body>
</html>
"""


PRIVACY = f"""<h1>Политика конфиденциальности</h1>
<p class="muted">Действует с 27 октября 2026 года</p>
<p>Документ описывает, какие данные обрабатывают Telegram-бот {BOT} («бот») и служебное приложение SaveBot Promo, которым владелец бота публикует свои ролики.</p>

<h2>1. Бот {BOT}</h2>
<ul>
<li><b>Что сохраняется.</b> После вашего согласия и подключения через «Автоматизацию чатов» бот сохраняет сообщения подключённых личных чатов (текст и медиа), чтобы вернуть вам удалённые и изменённые сообщения. Также хранятся ваш Telegram ID, имя и настройки бота.</li>
<li><b>Без согласия</b> бот ничего не сохраняет.</li>
<li><b>Защита.</b> Переписка хранится зашифрованной в закрытом месте, посторонние доступа к ней не имеют.</li>
<li><b>Не продаём и не передаём</b> данные третьим лицам, кроме случаев, прямо предусмотренных законом.</li>
<li><b>Срок хранения:</b> 30 дней, с Premium — до 6 месяцев; затем данные стираются автоматически.</li>
<li><b>Удаление:</b> «Личный кабинет» → «Удалить мои данные» → «Да, удалить всё». Данные стираются навсегда, из резервных копий — в течение 10 дней.</li>
<li><b>Оплата</b> проходит через Telegram Stars или криптовалютные сервисы; данные банковских карт бот не получает.</li>
</ul>

<h2>2. Приложение SaveBot Promo (YouTube, TikTok и другие площадки)</h2>
<ul>
<li>Приложением пользуется только владелец бота: оно загружает собственные рекламные ролики THE.SaveBot на собственные аккаунты бренда (YouTube, TikTok, VK и другие).</li>
<li>Доступ — только к аккаунтам бренда и только для загрузки роликов и чтения их статистики (просмотры). Данные других пользователей этих площадок не собираются.</li>
<li>Ключи доступа хранятся в зашифрованном виде на компьютере владельца и никому не передаются.</li>
<li>Данные YouTube обрабатываются по <a href="https://www.youtube.com/t/terms">Условиям использования YouTube</a> и <a href="https://policies.google.com/privacy">Политике конфиденциальности Google</a>. Отозвать доступ можно в <a href="https://myaccount.google.com/permissions">настройках безопасности Google</a>.</li>
</ul>

<h2>3. Сайт</h2>
<p>Сайт не использует cookies, счётчики и рекламу и не собирает данные посетителей.</p>

<h2>4. Связь</h2>
<p>Вопросы о данных — в боте {BOT}. Об изменениях политики сообщим в боте и на этой странице.</p>

{HR}
<h1>Privacy Policy</h1>
<p class="muted">Effective October 27, 2026</p>
<p>This policy covers the Telegram bot {BOT} (“the bot”) and SaveBot Promo, an internal tool the bot owner uses to publish the bot’s own promotional videos.</p>
<h2>1. The bot</h2>
<ul>
<li>Only after your consent and connection via Telegram Business chat automation, the bot stores messages of connected private chats (text and media) to show you deleted and edited messages. It also stores your Telegram ID, name and settings.</li>
<li>Data is stored encrypted, is never sold and is not shared with third parties except where required by law.</li>
<li>Retention: 30 days (up to 6 months with Premium), then deleted automatically. You can delete all your data at any time in the bot (“Account” → “Delete my data”); backups are purged within 10 days.</li>
<li>Payments go through Telegram Stars or crypto services; the bot never receives card details.</li>
</ul>
<h2>2. SaveBot Promo (YouTube, TikTok and other platforms)</h2>
<ul>
<li>Used solely by the bot owner to upload the brand’s own videos to the brand’s own accounts and to read those videos’ view statistics.</li>
<li>It does not collect data about other users of these platforms. Access tokens are stored encrypted on the owner’s computer and are never shared.</li>
<li>YouTube data is handled under the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a> and the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>. Access can be revoked in <a href="https://myaccount.google.com/permissions">Google security settings</a>.</li>
</ul>
<h2>3. Website</h2>
<p>This website uses no cookies, analytics or ads and collects no visitor data.</p>
<h2>4. Contact</h2>
<p>Via the bot {BOT}.</p>"""

TERMS = f"""<h1>Условия использования</h1>
<p class="muted">Действуют с 27 октября 2026 года</p>
<ol>
<li><b>Сервис.</b> THE.SaveBot — Telegram-бот, который сохраняет сообщения подключённых чатов пользователя и показывает удалённые и изменённые сообщения.</li>
<li><b>Согласие.</b> Пользуясь ботом, вы принимаете эти условия и <a href="privacy.html">Политику конфиденциальности</a>.</li>
<li><b>Законное использование.</b> Бот нужен для сохранения вашей собственной переписки. Запрещено использовать его для преследования, шантажа, распространения чужих личных данных и других незаконных целей. За использование сохранённых данных отвечает пользователь.</li>
<li><b>Тарифы.</b> Standard бесплатный и без срока. Premium платный, цены и сроки указаны в боте. Оплата Telegram Stars возвращается по правилам Telegram; при возврате снимаются оплаченные дни.</li>
<li><b>Доступность.</b> Сервис предоставляется «как есть». Мы стараемся, чтобы бот работал без перерывов, но не гарантируем сохранение каждого сообщения: это зависит от Telegram.</li>
<li><b>Ограничение доступа</b> возможно при нарушении этих условий или правил Telegram.</li>
<li><b>Изменения</b> условий объявляются в боте и на этой странице.</li>
<li><b>Связь</b> — в боте {BOT}.</li>
</ol>
{HR}
<h1>Terms of Service</h1>
<p class="muted">Effective October 27, 2026</p>
<ol>
<li>THE.SaveBot is a Telegram bot that stores messages of the user’s connected chats and shows deleted and edited messages.</li>
<li>By using the bot you accept these terms and the <a href="privacy.html">Privacy Policy</a>.</li>
<li>Use the bot only for your own conversations and only lawfully; harassment, blackmail and sharing other people’s personal data are prohibited. You are responsible for how you use saved data.</li>
<li>Standard is free with no time limit; Premium is paid, prices are shown in the bot. Telegram Stars refunds follow Telegram rules; refunded days are removed.</li>
<li>The service is provided “as is”; delivery of every message is not guaranteed as it depends on Telegram.</li>
<li>We may restrict access for violations of these terms or Telegram rules. Changes are announced in the bot and on this page.</li>
<li>SaveBot Promo, the owner’s internal publishing tool, is used only to upload the brand’s own videos to the brand’s own accounts.</li>
<li>Contact: {BOT}.</li>
</ol>"""

for name, title, body in (("privacy.html", "Политика конфиденциальности", PRIVACY),
                          ("terms.html", "Условия использования", TERMS)):
    (D / name).write_text(page(name, title, body), encoding="utf-8", newline="\n")
(D / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8", newline="\n")
urls = "".join(f"<url><loc>{SITE}{p}</loc></url>\n" for p in ("", "privacy.html", "terms.html"))
(D / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                               + urls + "</urlset>\n", encoding="utf-8", newline="\n")
(D / ".nojekyll").write_text("")
print("ok")
