<?php

/**
 * @file
 * Contains \Drupal\comment\Form\MorseConverter.
 */

namespace Drupal\morse\Form;

use Drupal\Core\Extension\ModuleHandlerInterface;
use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;
use Symfony\Component\DependencyInjection\ContainerInterface;

/**
 * Provides the comments overview administration form.
 */
class MorseConverter extends FormBase {

  /**
   * The module handler.
   *
   * @var \Drupal\Core\Extension\ModuleHandlerInterface
   */
  protected $moduleHandler;

  /**
   * Creates a CommentAdminOverview form.
   *
   * @param \Drupal\Core\Extension\ModuleHandlerInterface $module_handler
   *   The module handler.
   */
  public function __construct(ModuleHandlerInterface $module_handler) {
    $this->moduleHandler = $module_handler;
  }

  /**
   * {@inheritdoc}
   */
  public static function create(ContainerInterface $container) {
    return new static(
      $container->get('module_handler')
    );
  }

  /**
   * {@inheritdoc}
   */
  public function getFormId() {
    return 'morse_converter';
  }

  /**
   * Form constructor for the comment overview administration form.
   *
   * @param array $form
   *   An associative array containing the structure of the form.
   * @param \Drupal\Core\Form\FormStateInterface $form_state
   *   The current state of the form.
   * @param string $type
   *   The type of the overview form ('approval' or 'new').
   *
   * @return array
   *   The form structure.
   */
  public function buildForm(array $form, FormStateInterface $form_state, $type = 'morse') {
    $form['alphabet'] = array(
      '#type' => 'textarea',
      '#title' => $this->t('Enter the Code to be converted.'),
      '#required' => TRUE,
      '#description' => t("Please do not enter any special character other than A-Z and 0-9."),
    );

    $form['submit'] = array(
      '#type' => 'submit',
      '#value' => t('Convert'),
      '#weight' => 30,
    );

    return $form;
  }

  /**
   * {@inheritdoc}
   */
  public function submitForm(array &$form, FormStateInterface $form_state) {

    $alphabets = $form_state->getValue('alphabet');
    $output = $this->morseConvertToMorse($alphabets);
    drupal_set_message($this->t($output));
    $form_state->setRedirect('morse.morse');
  }

  /**
   * Function to convert alphanumeric to morse code.
   *
   * @param string $alphabets
   *   A string which needs to be converted into morse.
   *
   * @return output
   *   A string with morse code.
   */
  public function morseConvertToMorse($alphabets) {
    $output = "";
    $morse_codes = $this->morseAlphabets();
    $bigarr = str_split($alphabets);
    foreach ($bigarr as $key => $value) {
      if (array_key_exists($value, $morse_codes)) {
        $output .= $morse_codes[$value] . "  ";
      }
      elseif ($value == " ") {
        $output .= "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
      }
    }
    return $output;
  }

  /**
   * Helper function to get array of morse and alphanumeric words.
   *
   * @return array
   *   Array of morse codes.
   */
  public function morseAlphabets() {
    // Defined morse variables in array.
    return array(
      "A" => ".-",
      "B" => "-...",
      "C" => "-.-.",
      "D" => "-..",
      "E" => ".",
      "F" => "..-.",
      "G" => "--.",
      "H" => "....",
      "I" => "..",
      "J" => ".---",
      "K" => "-.-",
      "L" => ".-..",
      "M" => "--",
      "N" => "-.",
      "O" => "---",
      "P" => ".--.",
      "Q" => "--.-",
      "R" => ".-.",
      "S" => "...",
      "T" => "-",
      "U" => "..-",
      "V" => "...-",
      "W" => ".--",
      "X" => "-..-",
      "Y" => "-.--",
      "Z" => "--..",
      "a" => ".-",
      "b" => "-...",
      "c" => "-.-.",
      "d" => "-..",
      "e" => ".",
      "f" => "..-.",
      "g" => "--.",
      "h" => "....",
      "i" => "..",
      "j" => ".---",
      "k" => "-.-",
      "l" => ".-..",
      "m" => "--",
      "n" => "-.",
      "o" => "---",
      "p" => ".--.",
      "q" => "--.-",
      "r" => ".-.",
      "s" => "...",
      "t" => "-",
      "u" => "..-",
      "v" => "...-",
      "w" => ".--",
      "x" => "-..-",
      "y" => "-.--",
      "z" => "--..",
      "1" => ".----",
      "2" => "..---",
      "3" => "...--",
      "4" => "....-",
      "5" => ".....",
      "6" => "-....",
      "7" => "--...",
      "8" => "---..",
      "9" => "----.",
      "0" => "-----",
      "." => ".-.-.-",
      "," => "--..--",
      "?" => "..--..",
      "/" => "-..-.",
      "@" => ".--.-.",
    );
  }

}
