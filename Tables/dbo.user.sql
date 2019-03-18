CREATE TABLE [dbo].[user]
(
[id] [int] NOT NULL IDENTITY(1, 1),
[user_name] [varchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[password] [varchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[user] ADD CONSTRAINT [PK__user__3213E83FBB7349AC] PRIMARY KEY CLUSTERED  ([id]) ON [PRIMARY]
GO
