"""Doc control utils."""

try:
  import tf_doc_controls as doc_controls  # pylint: disable=g-direct-tensorflow-import,g-import-not-at-top
except ModuleNotFoundError:
  doc_controls = None

if doc_controls:

  do_not_doc_in_subclasses = doc_controls.do_not_doc_in_subclasses
  do_not_doc_inheritable = doc_controls.do_not_doc_inheritable
  do_not_generate_docs = doc_controls.do_not_generate_docs

else:

  def do_not_doc_in_subclasses(obj):
    return obj

  def do_not_doc_inheritable(obj):
    return obj

  def do_not_generate_docs(obj):
    return obj


EXTRA_DOCS = dict()


def documented(obj, doc):
  """Adds a docstring to typealias by overriding the `__doc__` attribute.
  Note: Overriding `__doc__` is only possible after python 3.7.
  Args:
    obj: Typealias object that needs to be documented.
    doc: Docstring of the typealias. It should follow the standard pystyle
      docstring rules.
  Returns:
    Documented variables.
  """
  if isinstance(obj, int) or obj in [(), None, ""]:
    raise ValueError(f"Can't add docs to singletons: `{obj}`.")
  try:
    obj.__doc__ = doc
  except AttributeError:
    EXTRA_DOCS[id(obj)] = doc
  return obj