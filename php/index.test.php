<?php 

use PHPUnit\Framework\TestCase;

class SommeChiffresTest extends TestCase {

    public function testSommeChiffres() {
        $this->assertEquals(sommeChiffres(12345), 15);
    }

    public function testSommeChiffresEntierNegatif() {
        $this->expectException(Exception::class);
        sommeChiffres(-123);
    }

    public function testSommeChiffresChaineCaracteres() {
        $this->expectException(Exception::class);
        sommeChiffres('abc');
    }

    public function testSommeChiffresNombreVirgule() {
        $this->expectException(Exception::class);
        sommeChiffres(12.345);
    }
}