<?php

/**
 * @file
 * Contains Drupal\morse\Controller.
 */

namespace Drupal\morse\Controller;

use Drupal\Core\Controller\ControllerBase;
use Drupal\Core\Form\FormBuilderInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\DependencyInjection\ContainerInterface;

/**
 * Provides the Morse converter Controller.
 */
class MorseController extends ControllerBase {

  /**
   * The form builder.
   *
   * @var \Drupal\Core\Form\FormBuilderInterface
   */
  protected $formBuilder;

  /**
   * {@inheritdoc}
   */
  public static function create(ContainerInterface $container) {
    return new static(
      $container->get('form_builder')
    );
  }

  /**
   * Constructs an FormBuilderInterface object.
   *
   * @param \Drupal\Core\Form\FormBuilderInterface $form_builder
   *   The form builder.
   */
  public function __construct(FormBuilderInterface $form_builder) {
    $this->formBuilder = $form_builder;
  }

  /**
   * Constructs a morse request object.
   */
  public function morse(Request $request, $type) {
    if ($type == "morse") {
      return $this->formBuilder->getForm('\Drupal\morse\Form\MorseConverter', $request);
    }
    else {
      return $this->formBuilder->getForm('\Drupal\morse\Form\AlphaNumericConverter', $request);
    }
  }

}
