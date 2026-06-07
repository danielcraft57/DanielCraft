<?php
/**
 * Chargement .env et en-têtes CORS JSON (partagé par les endpoints API).
 */

declare(strict_types=1);

function load_dotenv_if_present(array $paths): void
{
    foreach ($paths as $envPath) {
        if (!is_string($envPath) || $envPath === '' || !is_file($envPath) || !is_readable($envPath)) {
            continue;
        }
        $lines = @file($envPath, FILE_IGNORE_NEW_LINES);
        if (!is_array($lines)) {
            continue;
        }
        foreach ($lines as $rawLine) {
            $line = trim((string) $rawLine);
            if ($line === '' || str_starts_with($line, '#')) {
                continue;
            }
            if (!preg_match('/^([A-Za-z_][A-Za-z0-9_]*)=(.*)$/', $line, $m)) {
                continue;
            }
            $key = $m[1];
            $val = trim($m[2]);
            if (($val !== '') && (
                (str_starts_with($val, '"') && str_ends_with($val, '"')) ||
                (str_starts_with($val, "'") && str_ends_with($val, "'"))
            )) {
                $val = substr($val, 1, -1);
            }
            if (getenv($key) !== false && getenv($key) !== '') {
                continue;
            }
            putenv($key . '=' . $val);
            $_ENV[$key] = $val;
            $_SERVER[$key] = $val;
        }
        break;
    }
}

function api_bootstrap_env(): void
{
    load_dotenv_if_present([
        __DIR__ . '/../.env',
        __DIR__ . '/../../.env',
        getcwd() . '/.env',
    ]);
}

function api_apply_cors(): void
{
    $origin = isset($_SERVER['HTTP_ORIGIN']) ? (string) $_SERVER['HTTP_ORIGIN'] : '';
    if (preg_match('#^https?://(www\.)?danielcraft\.fr$#', $origin)) {
        header('Access-Control-Allow-Origin: ' . $origin);
    } elseif ($origin !== '' && preg_match('#^https?://(127\.0\.0\.1|localhost)(:\d+)?$#i', $origin)) {
        header('Access-Control-Allow-Origin: ' . $origin);
    }
    header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
    header('Access-Control-Allow-Headers: Content-Type');
}

function api_json_headers(): void
{
    header('Content-Type: application/json; charset=utf-8');
    header('X-Content-Type-Options: nosniff');
    api_apply_cors();
}

function api_site_base(): string
{
    $base = getenv('SITE_BASE') ?: 'https://danielcraft.fr';
    return rtrim((string) $base, '/');
}

/**
 * Journalisation légère (stderr PHP + fichier optionnel API_LOG_FILE).
 */
function api_log(string $channel, string $message, array $context = []): void
{
    $line = '[' . $channel . '] ' . $message;
    if ($context !== []) {
        $line .= ' ' . json_encode($context, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    }
    error_log($line);
    $logFile = getenv('API_LOG_FILE');
    if (is_string($logFile) && $logFile !== '') {
        @file_put_contents($logFile, gmdate('c') . ' ' . $line . "\n", FILE_APPEND | LOCK_EX);
    }
}
