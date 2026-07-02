<?php
/**
 * Modèle d’e-mail post-livraison (fidélisation Ch.8 — valeur prouvée).
 * Appel manuel ou via automatisation future (cron / Facturio webhook).
 */
declare(strict_types=1);

require_once __DIR__ . '/devis-notification.php';

/**
 * @param array{prenom?:string,site_url?:string,prestation?:string} $client
 */
function post_livraison_build_email(array $client): array
{
    $prenom = trim((string) ($client['prenom'] ?? ''));
    $salut = $prenom !== '' ? $prenom : 'Bonjour';
    $site = trim((string) ($client['site_url'] ?? ''));
    $prestation = trim((string) ($client['prestation'] ?? 'votre site'));

    $siteLine = $site !== '' ? "Votre site : {$site}\n" : '';

    $text = <<<TXT
{$salut},

Votre {$prestation} est en ligne depuis un mois — voici ce qu’on peut déjà regarder ensemble :

{$siteLine}- Visites et pages les plus consultées (Google Search Console)
- Demandes reçues via le formulaire ou le téléphone
- Points rapides à améliorer si besoin (texte, photo, mobile)

Le support inclus de 14 jours après livraison est terminé, mais vous pouvez toujours répondre à cet e-mail pour une question ponctuelle ou un entretien mensuel.

— Loïc Daniel, DanielCraft
03 87 78 09 16 · contact@danielcraft.fr
TXT;

    $siteHtml = $site !== ''
        ? '<p><strong>Votre site :</strong> <a href="' . htmlspecialchars($site, ENT_QUOTES, 'UTF-8') . '">'
            . htmlspecialchars($site, ENT_QUOTES, 'UTF-8') . '</a></p>'
        : '';

    $html = '<p>' . htmlspecialchars($salut, ENT_QUOTES, 'UTF-8') . ',</p>'
        . '<p>Votre <strong>' . htmlspecialchars($prestation, ENT_QUOTES, 'UTF-8')
        . '</strong> est en ligne depuis un mois — voici ce qu’on peut déjà regarder ensemble :</p>'
        . $siteHtml
        . '<ul>'
        . '<li>Visites et pages les plus consultées (Google Search Console)</li>'
        . '<li>Demandes reçues via le formulaire ou le téléphone</li>'
        . '<li>Points rapides à améliorer si besoin (texte, photo, mobile)</li>'
        . '</ul>'
        . '<p>Le support inclus de 14 jours après livraison est terminé, mais vous pouvez toujours répondre à cet e-mail pour une question ponctuelle ou un entretien mensuel.</p>'
        . '<p>— Loïc Daniel, DanielCraft<br>03 87 78 09 16 · contact@danielcraft.fr</p>';

  return [
        'subject' => 'Votre site après 1 mois — ce qu’on peut mesurer',
        'text' => $text,
        'html' => $html,
    ];
}

/**
 * Envoie l’e-mail post-livraison à un client.
 */
function post_livraison_send(string $to, array $client): bool
{
    $mail = post_livraison_build_email($client);
    return devis_send_simple_mail($to, $mail['subject'], $mail['text'], $mail['html']);
}
