# General notes and design principles

## Decoupled development

Assume poor communication between Cherwell admins and users of this package. Be able to handle unexpected schema changes, within reason.

(_N.B._ This design principle is not a reflection of my personal experience with Cherwell admins.)

### Consequences

To deal with schema changes, autogenerate Pydantic models from Business Objects and maintain them in a separate git repository. Ensure that schema changes result in understandable diffs.

If we have API access to both the staging and production Cherwell instances, take advantage of this (schema changes will probably appear in staging and then move to production).


## Code generation vs. runtime type construction

Prefer code generation **if** it offers advantages such as:

-   Subclassing classes with mypy/pylance type checking in IDE
-   Faster startup - this package might be used for short-lived scripts that are called often
-   Developer understanding

Generated code should be as human readable as possible. It should be stable enough to be version controlled such that CVS changes make sense to the observer.

## Multiple instances

Must be able to connect to multiple Cherwell instances at the same time. Use cases: comparing test and production schemas, transferring / comparing business objects between instances.

## asyncio

Async first development because my use case requires it. A sync overlay could be considered.

## pydantic

Make full use of Pydantic's features and approach.

## Developer experience

- Type hinting for a better IDE experience
- Discoverability
- ipython helpers (repr, autocomplete)

## Other

- swagger source: https://cherwell-be-prod.cherwell.com/bundle/cherwell_rest_api_10_5_help_only/page/content/api/csm_api-swagger.json
