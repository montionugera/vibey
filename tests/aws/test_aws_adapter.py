import pytest

from vibey.infrastructure.aws.adapter import AwsClientAdapter
from vibey.application.interfaces.azure import CloudClientPort


def test_aws_adapter_implements_protocol() -> None:
    adapter: CloudClientPort = AwsClientAdapter()
    assert isinstance(adapter, CloudClientPort)


@pytest.mark.asyncio
async def test_aws_adapter_methods_raise() -> None:
    adapter = AwsClientAdapter()
    from vibey.domain.deployment import AzureTargetScope

    scope = AzureTargetScope("t", "s", "rg", "dev", "eu")
    # The methods are async; they should raise NotImplementedError.
    import pytest
    with pytest.raises(NotImplementedError):
        await adapter.discover_environment(scope)
    with pytest.raises(NotImplementedError):
        await adapter.execute_plan(scope, None)  # type: ignore[arg-type]
    with pytest.raises(NotImplementedError):
        await adapter.get_resource_status(scope, "res")
    with pytest.raises(NotImplementedError):
        await adapter.delete_resource(scope, "res", None)  # type: ignore[arg-type]
