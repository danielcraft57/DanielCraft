<?php

declare(strict_types=1);

namespace DanielCraft\Tests;

use PHPUnit\Framework\TestCase;

final class EnvTest extends TestCase
{
    protected function setUp(): void
    {
        require_once DANIELCRAFT_REPO_ROOT . '/api/env.php';
    }

    public function test_load_dotenv_sets_missing_variables(): void
    {
        $tmp = tempnam(sys_get_temp_dir(), 'dc-env-');
        self::assertIsString($tmp);
        file_put_contents($tmp, "PHPUNIT_TMP_VAR=test_value_123\n# comment\nINVALID LINE\n");

        $key = 'PHPUNIT_TMP_VAR';
        $previous = getenv($key);
        putenv($key);
        unset($_ENV[$key], $_SERVER[$key]);

        try {
            load_dotenv_if_present([$tmp]);
            self::assertSame('test_value_123', getenv($key));
        } finally {
            if ($previous !== false) {
                putenv($key . '=' . $previous);
                $_ENV[$key] = $previous;
                $_SERVER[$key] = $previous;
            } else {
                putenv($key);
                unset($_ENV[$key], $_SERVER[$key]);
            }
            @unlink($tmp);
        }
    }

    public function test_site_base_trims_trailing_slash(): void
    {
        $previous = getenv('SITE_BASE');
        putenv('SITE_BASE=https://danielcraft.fr/');
        $_ENV['SITE_BASE'] = 'https://danielcraft.fr/';
        $_SERVER['SITE_BASE'] = 'https://danielcraft.fr/';

        try {
            self::assertSame('https://danielcraft.fr', api_site_base());
        } finally {
            if ($previous !== false) {
                putenv('SITE_BASE=' . $previous);
                $_ENV['SITE_BASE'] = $previous;
                $_SERVER['SITE_BASE'] = $previous;
            } else {
                putenv('SITE_BASE');
                unset($_ENV['SITE_BASE'], $_SERVER['SITE_BASE']);
            }
        }
    }
}
