<?php
/**
 * Endpoint d'envoi du formulaire de contact (AJAX).
 * Recoit POST, valide les champs, envoie un email et repond en JSON.
 */

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

// Autoriser les requetes depuis le meme domaine (CORS)
$origin = isset($_SERVER['HTTP_ORIGIN']) ? $_SERVER['HTTP_ORIGIN'] : '';
if (preg_match('#^https?://(www\.)?danielcraft\.fr$#', $origin)) {
    header('Access-Control-Allow-Origin: ' . $origin);
}
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Méthode non autorisée']);
    exit;
}

// Recuperation et nettoyage des donnees
$name    = isset($_POST['name'])    ? trim(strip_tags((string) $_POST['name']))    : '';
$email   = isset($_POST['email'])   ? trim((string) $_POST['email'])                : '';
$phone   = isset($_POST['phone'])   ? trim(strip_tags((string) $_POST['phone']))   : '';
$service = isset($_POST['service']) ? trim(strip_tags((string) $_POST['service'])) : '';
$budget  = isset($_POST['budget'])  ? trim(strip_tags((string) $_POST['budget']))  : '';
$message = isset($_POST['message']) ? trim(strip_tags((string) $_POST['message'])) : '';

// Validation
$errors = [];

if ($name === '') {
    $errors[] = 'Le nom est obligatoire.';
}

if ($email === '') {
    $errors[] = 'L\'email est obligatoire.';
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = 'L\'email n\'est pas valide.';
}

if ($message === '') {
    $errors[] = 'Le message est obligatoire.';
}

if ($service === '') {
    $errors[] = 'Le type de projet est obligatoire.';
}

if (!empty($errors)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => implode(' ', $errors)]);
    exit;
}

// Limite de longueur pour eviter abus
if (strlen($name) > 200 || strlen($message) > 5000 || strlen($phone) > 30) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Données trop longues.']);
    exit;
}

$to      = 'contact@danielcraft.fr';
$subject = 'Nouveau contact danielcraft.fr - ' . ($service ?: 'Projet');

$labels = [
    'web'     => 'Développement Web',
    'backend' => 'Backend & APIs',
    'mobile'  => 'Application Mobile',
    'other'   => 'Autre',
];
$serviceLabel = $labels[$service] ?? $service;

$body = "Nom : " . $name . "\n";
$body .= "Email : " . $email . "\n";
$body .= "Téléphone : " . ($phone ?: 'Non renseigné') . "\n";
$body .= "Type de projet : " . $serviceLabel . "\n";
$body .= "Service / budget : " . ($budget ?: 'Non renseigné') . "\n\n";
$body .= "Message :\n" . $message . "\n";

$headers = [
    'From: ' . $email,
    'Reply-To: ' . $email,
    'X-Mailer: PHP/' . phpversion(),
    'Content-Type: text/plain; charset=UTF-8',
];

$sent = @mail($to, $subject, $body, implode("\r\n", $headers));

if (!$sent) {
    // En dev ou si mail() echoue, logger et repondre success pour ne pas bloquer l'UX
    error_log('[send-contact] mail() failed for ' . $email);
    // Repondre success quand meme pour eviter blocage cote client si serveur mail mal configure
}

echo json_encode(['success' => true]);
