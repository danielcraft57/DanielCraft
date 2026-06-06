<?php

declare(strict_types=1);

/**
 * Catalogue prestations (api/data/prestations.json, copié au build).
 */

function prestations_catalog_path(): string
{
    return __DIR__ . '/data/prestations.json';
}

/**
 * @return array{categories: array<int, array<string, mixed>>, items: array<int, array<string, mixed>>}
 */
function prestations_load_catalog(): array
{
    $empty = ['categories' => [], 'items' => []];
    $path = prestations_catalog_path();
    if (!is_file($path)) {
        return $empty;
    }
    $raw = file_get_contents($path);
    if ($raw === false) {
        return $empty;
    }
    $data = json_decode($raw, true);
    if (!is_array($data)) {
        return $empty;
    }
    $data['categories'] = isset($data['categories']) && is_array($data['categories']) ? $data['categories'] : [];
    $data['items'] = isset($data['items']) && is_array($data['items']) ? $data['items'] : [];
    return $data;
}

/**
 * @return array<string, mixed>|null
 */
function prestations_find_by_slug(string $slug): ?array
{
    $slug = trim($slug);
    if ($slug === '') {
        return null;
    }
    foreach (prestations_load_catalog()['items'] as $item) {
        if (!is_array($item)) {
            continue;
        }
        if (($item['slug'] ?? '') === $slug) {
            return $item;
        }
    }
    return null;
}

/**
 * @return array<string, mixed>|null
 */
function prestations_find_by_service_slug(string $serviceSlug): ?array
{
    $serviceSlug = trim($serviceSlug);
    if ($serviceSlug === '') {
        return null;
    }
    foreach (prestations_load_catalog()['items'] as $item) {
        if (!is_array($item)) {
            continue;
        }
        if (($item['service_slug'] ?? '') === $serviceSlug) {
            return $item;
        }
    }
    return null;
}
