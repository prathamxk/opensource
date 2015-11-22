<?php

/**
 * @file
 * Contains \Drupal\morse\Form\AlphaNumericConverter.
 */

namespace Drupal\morse\Form;

use Drupal\Core\Extension\ModuleHandlerInterface;
use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;
use Symfony\Component\DependencyInjection\ContainerInterface;

/**
 * Provides the Alphanumeric converter form.
 */
class AlphaNumericConverter extends FormBase {

  /**
   * The module handler.
   *
   * @var \Drupal\Core\Extension\ModuleHandlerInterface
   */
  protected $moduleHandler;

  /**
   * Creates a Alphanumeric converter form.
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
    return 'alphanumeric_converter';
  }

  /**
   * Form constructor for the cAlphanumeric converter form.
   *
   * @param array $form
   *   An associative array containing the structure of the form.
   * @param \Drupal\Core\Form\FormStateInterface $form_state
   *   The current state of the form.
   * @param string $type
   *   The type of the overview form ('morse' or 'alpha').
   *
   * @return array
   *   The form structure.
   */
  public function buildForm(array $form, FormStateInterface $form_state, $type = 'alpha') {

    $form['morse'] = array(
      '#type' => 'textarea',
      '#title' => t('Enter the morse code here.'),
      '#required' => TRUE,
      '#description' => t("Enter the valid morse code to avoid wrong ouput."),
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

    $morsecode = $form_state->getValue('morse');
    $output = $this->morseConvertToAlpha($morsecode);
    drupal_set_message($this->t($output));
    $form_state->setRedirect('morse.alpha');
  }

  /**
   * Function to convert morse to alphanumeric language.
   *
   * @param string $morsecode
   *   A string in morse format which needs to be converted into alphanumeric.
   *
   * @return output
   *   A string Alphanumeric value of morse code.
   */
  public function morseConvertToAlpha($morsecode) {
    $output = "";
    $morse_codes = $this->morseAlphabets();
    $alpha = explode("       ", $morsecode);
    foreach ($alpha as $key => $value) {
      if ($value) {
        $innerword = explode(" ", $value);
        foreach ($innerword as $k => $v) {
          if (in_array($v, $morse_codes)) {
            $output .= array_search($v, $morse_codes);
          }
          else {
            $output .= "";
          }
        }
        $output .= " ";
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
