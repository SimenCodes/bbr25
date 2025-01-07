using BoardGameServer.Application.Services;
using BoardGameServerSimple.Endpoints;
using BoardGameServerSimple.Services;
using Negotiator;
using Scalar.AspNetCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi
builder.Services.AddOpenApi();
builder.Services.AddSingleton<ValidationRules>();
builder.Services.AddSingleton<GameService>();
builder.Services.AddSingleton<INegotiationService, NegotiationService>();
builder.Services.AddSingleton<IMessageValidator, MessageValidator>();

var app = builder.Build();

app.MapOpenApi();
app.MapGameBoardEndpoints();
app.MapPlayerEndpoints();
app.MapNegotiationEndpoints();

if (app.Environment.IsDevelopment())
{
    app.MapScalarApiReference(options =>
    {
        options
        .WithTitle("Board Game Server")
        .WithTheme(ScalarTheme.Mars)
        .WithDefaultHttpClient(ScalarTarget.CSharp, ScalarClient.HttpClient);
    });
}

app.UseHttpsRedirection();
app.Run();
